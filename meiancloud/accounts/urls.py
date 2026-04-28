from django.urls import path

from .views import (
    changepsw_view,
    delete_account,
    editprofile_view,
    login_view,
    logout_view,
    register_view,
    user_profile_view,
)


app_name = "accounts"

urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path("profile/<int:userid>/", user_profile_view, name="userprofile"),
    path("changepsw/<int:userid>/", changepsw_view, name="changepsw"),
    path("editprofile/<int:userid>/", editprofile_view, name="editprofile"),
    path("delete_account/", delete_account, name="delete_account"),
]
