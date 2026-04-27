from django.urls import path

from . import views_accounts


urlpatterns = [
    path("login/", views_accounts.login_view, name="login"),
    path("register/", views_accounts.register_view, name="register"),
    path("logout/", views_accounts.logout_view, name="logout"),
    path("profile/<int:userid>/", views_accounts.user_profile_view, name="userprofile"),
    path("changepsw/<int:userid>/", views_accounts.changepsw_view, name="changepsw"),
    path("editprofile/<int:userid>/", views_accounts.editprofile_view, name="editprofile"),
    path("delete_account/", views_accounts.delete_account, name="delete_account"),
]
