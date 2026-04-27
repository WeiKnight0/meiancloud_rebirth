from django.urls import path

from . import views_ai


urlpatterns = [
    path("api/chat/", views_ai.chat_api, name="chat_api"),
]
