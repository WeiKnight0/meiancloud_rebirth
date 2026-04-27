from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .context import default_context
from .forms_community import CommentForm, ReplyForm
from .models import Comment, UserProfile


def freetotalk_view(request: HttpRequest):
    comment_form = None
    reply_form = None
    if request.method == "POST":
        action_type = request.POST.get("action_type")
        if action_type == "action1":
            comment_form = CommentForm(request.POST)
            reply_form = ReplyForm()
            if comment_form.is_valid():
                if request.user.is_authenticated and (not request.user.is_superuser):
                    user_profile = UserProfile.objects.get(owner=request.user)
                    Comment.objects.create(
                        owner=user_profile,
                        title=request.POST.get("title"),
                        content=request.POST.get("content"),
                        parent_comment=None,
                    )
                    return JsonResponse({"success": True})
                return redirect("home:login_prompt")
            return JsonResponse({"success": False, "errors": comment_form.errors})

        comment_form = CommentForm()
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            if request.user.is_authenticated and (not request.user.is_superuser):
                comment = get_object_or_404(Comment, id=request.POST.get("comment_id"))
                user_profile = UserProfile.objects.get(owner=request.user)
                Comment.objects.create(
                    owner=user_profile,
                    title=None,
                    content=reply_form.cleaned_data["reply_content"],
                    parent_comment=comment,
                )
                return JsonResponse({"success": True, "action": "reply"})
            return redirect("home:login_prompt")
        return JsonResponse({"success": False, "errors": reply_form.errors})

    if request.method == "DELETE":
        try:
            comment = get_object_or_404(Comment, id=request.GET.get("comment_id"))
            if comment.parent_comment is None:
                comment.replies.all().delete()
            comment.delete()
            return JsonResponse({"status": "success", "message": "评论删除成功"})
        except Exception as exc:
            return JsonResponse({"status": "error", "message": str(exc)}, status=500)

    comment_form = CommentForm()
    reply_form = ReplyForm()
    comment_list = (
        Comment.objects.all()
        .filter(parent_comment__isnull=True, is_checked=True)
        .select_related("owner__owner")
        .prefetch_related("replies")
        .order_by("-id")
    )
    for comment in comment_list:
        comment.filtered_replies = comment.replies.filter(is_checked=True)

    comments = Paginator(comment_list, 5).get_page(request.GET.get("page"))
    context = default_context(request)
    context.update(
        {"comment_form": comment_form, "comments": comments, "reply_form": reply_form}
    )
    return render(request, "home/freetotalk.html", context)


@user_passes_test(lambda user: user.is_superuser)
def comment_management(request: HttpRequest):
    if request.method == "POST":
        if "approve" in request.POST:
            comment = get_object_or_404(Comment, id=request.POST.get("comment_id"))
            comment.is_checked = True
            comment.save()
        elif "delete" in request.POST:
            comment = get_object_or_404(Comment, id=request.POST.get("comment_id"))
            if comment.parent_comment is None:
                comment.replies.all().delete()
            comment.delete()

    comments = Comment.objects.all().order_by("-id")
    context = default_context(request)
    context.update({"comments": comments})
    return render(request, "home/comment_management.html", context)
