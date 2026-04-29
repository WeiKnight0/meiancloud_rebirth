import os
import shutil

from django.conf import settings
from django.contrib.auth.models import User
from django.db import transaction


def delete_user_and_files(user: User):
    """删除用户及其相关文件"""
    user_id = user.id
    user_media_path = os.path.join(settings.MEDIA_ROOT, "accounts", "user_img", str(user_id))
    # 事务内完成数据库删除，文件清理放在事务外做容错。
    with transaction.atomic():
        user.delete()
    if os.path.exists(user_media_path):
        shutil.rmtree(user_media_path, ignore_errors=True)
    return True
