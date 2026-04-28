from django.db import models

from accounts.models import UserProfile


class Comment(models.Model):
    owner = models.ForeignKey(
        to=UserProfile,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="comment_user",
    )
    title = models.TextField(max_length=50, blank=True, null=True)
    content = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="replies",
    )
    is_checked = models.BooleanField(verbose_name="is_checked", null=False, default=False, blank=False)

    def __str__(self):
        return str(self.title)
