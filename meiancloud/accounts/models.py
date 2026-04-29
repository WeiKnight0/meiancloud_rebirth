import os

from django.contrib.auth.models import User
from django.db import models
from django.templatetags.static import static


def user_directory_path(instance, filename) -> str:
    # 头像按用户 id 固定命名，便于覆盖旧头像和集中管理文件。
    ext = filename.split(".")[-1]
    filename = f"{instance.owner.id}.{ext}"
    return os.path.join("accounts", "user_img", str(instance.owner.id), filename)


class UserProfile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="用户")
    nick_name = models.CharField("昵称", max_length=20, blank=True, default="")
    USER_GENDER_TYPE = (
        ("0", "请选择"),
        ("male", "男"),
        ("female", "女"),
        ("others", "其他"),
    )
    gender = models.CharField("性别", max_length=8, choices=USER_GENDER_TYPE, default="0")
    birthday = models.DateField("出生日期", null=True, blank=True)
    image = models.ImageField(
        verbose_name="头像",
        upload_to=user_directory_path,
        max_length=100,
        blank=True,
        null=True,
    )
    sign = models.TextField("个性签名", max_length=100, null=True, blank=True, default="")

    def save(self, *args, **kwargs):
        # 新头像上传后删除旧文件，避免媒体目录残留历史图片。
        if self.pk:
            old_instance = UserProfile.objects.get(pk=self.pk)
            if old_instance.image and self.image != old_instance.image:
                old_instance.image.delete(save=False)
        super().save(*args, **kwargs)

    @property
    def avatar_url(self):
        # 未上传头像时统一回退到默认图片。
        if self.image:
            return self.image.url
        return static("accounts/img/default.png")

    def __str__(self):
        return self.owner.username
