from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.TextField(blank=True, max_length=50, null=True)),
                ("content", models.TextField(max_length=200)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "is_checked",
                    models.BooleanField(default=False, verbose_name="is_checked"),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="accounts.userprofile",
                        verbose_name="comment_user",
                    ),
                ),
                (
                    "parent_comment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="replies",
                        to="community.comment",
                    ),
                ),
            ],
        )
    ]
