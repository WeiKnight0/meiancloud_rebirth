from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from core.context import default_context

from .forms import ChangePasswordForm, LoginForm, RegisterForm, UserProfileForm
from .models import UserProfile
from .services import delete_user_and_files


def login_view(request: HttpRequest):
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
    success = False
    if request.method != "POST":
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
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
    context = default_context(request)
    context.update({"form": form, "success": success})
    return render(request, "accounts/register.html", context)


def logout_view(request: HttpRequest):
    logout(request)
    return redirect("core:index")


def user_profile_view(request: HttpRequest, userid: int):
    if request.user.is_authenticated and request.user.id == userid and (not request.user.is_superuser):
        user_profile = get_object_or_404(UserProfile, owner=request.user)
        context = default_context(request)
        context.update(
            {
                "current_userprofile": user_profile,
                "current_user": get_object_or_404(User, id=userid),
            }
        )
        return render(request, "accounts/userprofile.html", context)

    user = get_object_or_404(User, id=userid)
    user_profile = get_object_or_404(UserProfile, owner=user)
    context = default_context(request)
    context.update({"current_userprofile": user_profile, "current_user": user})
    return render(request, "accounts/userprofile.html", context)


@login_required(login_url="accounts:login")
def changepsw_view(request: HttpRequest, userid: int):
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
    if request.user.id != userid:
        return redirect("core:login_prompt")

    success = False
    user_profile = get_object_or_404(UserProfile, owner=request.user)
    if request.method == "POST":
        form = UserProfileForm(request.POST, userprofile=user_profile)
        if form.is_valid():
            user_profile.nick_name = form.cleaned_data["nick_name"]
            user_profile.gender = form.cleaned_data["gender"]
            user_profile.birthday = form.cleaned_data["birthday"]
            user_profile.sign = form.cleaned_data["sign"]
            if "image" in request.FILES:
                user_profile.image = request.FILES["image"]
            user_profile.save()
            success = True
    else:
        form = UserProfileForm(userprofile=user_profile)

    context = default_context(request)
    context.update({"form": form, "userprofile": user_profile, "success": success})
    return render(request, "accounts/editprofile.html", context)


@login_required(login_url="accounts:login")
def delete_account(request: HttpRequest):
    if request.method == "POST":
        password = request.POST.get("password")
        user = request.user
        if authenticate(username=user.username, password=password):
            if delete_user_and_files(user):
                logout(request)
                return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "error": "密码错误"})
    return JsonResponse({"success": False, "error": "无效请求"})
