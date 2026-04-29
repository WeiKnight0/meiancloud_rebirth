from django.urls import path

from .views import (
    comment_create,
    comment_delete,
    comment_management,
    freetotalk_page,
    reply_create,
)


app_name = "community"

urlpatterns = [
    path("freetotalk/", freetotalk_page, name="freetotalk"),
    path("api/comments/", comment_create, name="comment_create"),
    path("api/comments/<int:comment_id>/", comment_delete, name="comment_delete"),
    path("api/comments/<int:comment_id>/replies/", reply_create, name="reply_create"),
    path("comment-management/", comment_management, name="comment-management"),
]
