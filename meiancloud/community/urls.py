from django.urls import path

from .views import comment_management, freetotalk_view


app_name = "community"

urlpatterns = [
    path("freetotalk/", freetotalk_view, name="freetotalk"),
    path("comment-management/", comment_management, name="comment-management"),
]
