from django.urls import path

from . import views_community


urlpatterns = [
    path("freetotalk/", views_community.freetotalk_view, name="freetotalk"),
    path(
        "comment-management/",
        views_community.comment_management,
        name="comment-management",
    ),
]
