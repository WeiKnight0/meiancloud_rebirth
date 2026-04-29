from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.db.models import Prefetch
from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from accounts.models import UserProfile
from core.context import default_context

from .forms import CommentForm, ReplyForm
from .models import Comment


def freetotalk_page(request: HttpRequest):
    # 仅负责页面渲染，表单和评论数据通过模板内 AJAX 与独立 API 交互。
    comment_form = CommentForm()
    reply_form = ReplyForm()
    comment_list = (
        Comment.objects.filter(parent_comment__isnull=True, is_checked=True)
        .select_related("owner__owner")
        .prefetch_related(
            Prefetch(
                "replies",
                queryset=Comment.objects.filter(is_checked=True).select_related("owner__owner"),
                to_attr="visible_replies",
            )
        )
        .order_by("-id")
    )

    comments = Paginator(comment_list, 5).get_page(request.GET.get("page"))
    context = default_context(request)
    context.update(
        {"comment_form": comment_form, "comments": comments, "reply_form": reply_form}
    )
    return render(request, "community/freetotalk.html", context)


@login_required(login_url="core:login_prompt")
@require_POST
def comment_create(request: HttpRequest):
    if request.user.is_superuser:
        return JsonResponse({"success": False, "error": "管理员无需发表评论"}, status=403)
    form = CommentForm(request.POST)
    if not form.is_valid():
        return JsonResponse({"success": False, "error": form.errors}, status=400)
    user_profile = UserProfile.objects.get(owner=request.user)
    Comment.objects.create(
        owner=user_profile,
        title=form.cleaned_data["title"],
        content=form.cleaned_data["content"],
        parent_comment=None,
    )
    return JsonResponse({"success": True})


@login_required(login_url="core:login_prompt")
@require_POST
def reply_create(request: HttpRequest):
    if request.user.is_superuser:
        return JsonResponse({"success": False, "error": "管理员无需发表回复"}, status=403)
    form = ReplyForm(request.POST)
    if not form.is_valid():
        return JsonResponse({"success": False, "error": form.errors}, status=400)
    comment = get_object_or_404(Comment, id=request.POST.get("comment_id"))
    user_profile = UserProfile.objects.get(owner=request.user)
    Comment.objects.create(
        owner=user_profile,
        title=None,
        content=form.cleaned_data["reply_content"],
        parent_comment=comment,
    )
    return JsonResponse({"success": True})


@login_required(login_url="core:login_prompt")
def comment_delete(request: HttpRequest, comment_id: int):
    if request.method != "DELETE":
        return JsonResponse({"success": False, "error": "方法不允许"}, status=405)
    comment = get_object_or_404(
        Comment.objects.select_related("owner__owner"), id=comment_id
    )
    if comment.owner.owner_id != request.user.id and not request.user.is_superuser:
        return JsonResponse({"success": False, "error": "无权删除该评论"}, status=403)
    if comment.parent_comment is None:
        # 删除主评论时一并删除其回复，避免悬挂数据。
        comment.replies.all().delete()
    comment.delete()
    return JsonResponse({"success": True})


@user_passes_test(lambda user: user.is_superuser)
def comment_management(request: HttpRequest):
    # 超级管理员在同一页面完成评论审核与删除。
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

    comments = Comment.objects.select_related("owner__owner", "parent_comment").order_by("-id")
    context = default_context(request)
    context.update({"comments": comments})
    return render(request, "community/comment_management.html", context)
