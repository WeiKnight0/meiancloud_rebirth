from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError, transaction
from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from core.context import default_context

from .forms import ChangePasswordForm, LoginForm, RegisterForm, UserProfileForm
from .models import UserProfile
from .services import delete_user_and_files


from django.views.decorators.http import require_POST


def login_view(request: HttpRequest):
    # 登录页同时承担表单展示和登录校验。
    success = False
    if request.method != "POST":
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                success = True
            else:
                form.add_error(field=None, error="用户名或密码错误！")
    context = default_context(request)
    context.update({"form": form, "success": success})
    return render(request, "accounts/login.html", context)


def register_view(request: HttpRequest):
    # 注册成功后立即创建资料并自动登录。
    success = False
    if request.method != "POST":
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = User.objects.create_user(
                        username=form.cleaned_data["username"],
                        password=form.cleaned_data["password"],
                        email=form.cleaned_data["email"],
                    )
                    UserProfile.objects.create(
                        owner=user,
                        nick_name=form.cleaned_data["nick_name"],
                        gender=form.cleaned_data["gender"],
                        birthday=form.cleaned_data["birthday"],
                    )
                login(request, user)
                success = True
            except IntegrityError:
                form.add_error("username", "用户名已存在")
    context = default_context(request)
    context.update({"form": form, "success": success})
    return render(request, "accounts/register.html", context)


@require_POST
def logout_view(request: HttpRequest):
    logout(request)
    return redirect("core:index")


def user_profile_view(request: HttpRequest, userid: int):
    user = get_object_or_404(User, id=userid)
    user_profile = get_object_or_404(UserProfile, owner=user)
    # 仅本人可查看邮箱、生日、签名等私密字段
    show_private = request.user.is_authenticated and request.user.id == userid
    context = default_context(request)
    context.update({
        "current_userprofile": user_profile,
        "current_user": user,
        "show_private": show_private,
    })
    return render(request, "accounts/userprofile.html", context)


@login_required(login_url="accounts:login")
def changepsw_view(request: HttpRequest, userid: int):
    # 仅允许本人修改密码，成功后强制重新登录。
    if request.user.id != userid:
        return redirect("core:login_prompt")

    success = False
    if request.method == "POST":
        form = ChangePasswordForm(request.POST, user=request.user)
        if form.is_valid():
            user = request.user
            user.set_password(form.cleaned_data["new1"])
            user.save()
            success = True
            logout(request)
    else:
        form = ChangePasswordForm()

    context = default_context(request)
    context.update({"form": form, "success": success})
    return render(request, "accounts/changepassword.html", context)


@login_required(login_url="core:login_prompt")
def editprofile_view(request: HttpRequest, userid: int):
    # 个人资料编辑只允许本人操作，头像更新时由模型层负责清理旧文件。
    if request.user.id != userid:
        return redirect("core:login_prompt")

    success = False
    user_profile = get_object_or_404(UserProfile, owner=request.user)
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, userprofile=user_profile)
        if form.is_valid():
            user_profile.nick_name = form.cleaned_data["nick_name"]
            user_profile.gender = form.cleaned_data["gender"]
            user_profile.birthday = form.cleaned_data["birthday"]
            user_profile.sign = form.cleaned_data["sign"]
            if form.cleaned_data.get("image"):
                user_profile.image = form.cleaned_data["image"]
            user_profile.save()
            success = True
    else:
        form = UserProfileForm(userprofile=user_profile)

    context = default_context(request)
    context.update({"form": form, "userprofile": user_profile, "success": success})
    return render(request, "accounts/editprofile.html", context)


@login_required(login_url="accounts:login")
def delete_account(request: HttpRequest):
    # 注销前要求用户再次输入密码，降低误删风险。
    if request.method != "POST":
        return JsonResponse({"success": False, "error": "无效请求"}, status=405)

    user = request.user
    password = request.POST.get("password")
    if authenticate(request, username=user.username, password=password) is None:
        return JsonResponse({"success": False, "error": "密码错误"}, status=400)
    if not delete_user_and_files(user):
        return JsonResponse({"success": False, "error": "注销失败"}, status=500)

    logout(request)
    return JsonResponse({"success": True})
