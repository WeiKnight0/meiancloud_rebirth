from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

import accounts.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nick_name", models.CharField(blank=True, default="", max_length=20, verbose_name="昵称")),
                (
                    "gender",
                    models.CharField(
                        choices=[("0", "请选择"), ("male", "男"), ("female", "女"), ("others", "其他")],
                        default="0",
                        max_length=8,
                        verbose_name="性别",
                    ),
                ),
                ("birthday", models.DateField(blank=True, null=True, verbose_name="出生日期")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default="accounts/user_img/default.png",
                        max_length=100,
                        null=True,
                        upload_to=accounts.models.user_directory_path,
                        verbose_name="头像",
                    ),
                ),
                (
                    "sign",
                    models.TextField(blank=True, default="", max_length=100, null=True, verbose_name="个性签名"),
                ),
                (
                    "owner",
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name="用户"),
                ),
            ],
        )
    ]
