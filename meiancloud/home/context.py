from django.http import HttpRequest

from .models import UserProfile


def get_userprofile(request: HttpRequest):
    """由request获取昵称"""
    nickname = None
    user_profile = None
    if request.user.is_authenticated and (not request.user.is_superuser):
        try:
            user_profile = UserProfile.objects.get(owner=request.user)
            nickname = user_profile.nick_name
        except UserProfile.DoesNotExist:
            nickname = "None"
    elif request.user.is_superuser:
        nickname = request.user.username
    return nickname, user_profile


def default_context(request: HttpRequest):
    nickname, userprofile = get_userprofile(request)
    return {
        "nick_name": nickname,
        "user": request.user,
        "userprofile": userprofile,
    }
