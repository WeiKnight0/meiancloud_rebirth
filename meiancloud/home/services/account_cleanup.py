import os
import shutil

from django.conf import settings
from django.contrib.auth.models import User

from ..models import UserProfile


def delete_user_and_files(user: User):
    """删除用户及其相关文件"""
    user_media_path = os.path.join(settings.MEDIA_ROOT, "home", "user_img", str(user.id))
    if os.path.exists(user_media_path):
        shutil.rmtree(user_media_path)

    user.delete()

    try:
        UserProfile.objects.get(owner=user)
        return False
    except UserProfile.DoesNotExist:
        return True
