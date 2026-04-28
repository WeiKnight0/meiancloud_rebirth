from django.urls import path

from .views import chat_api


app_name = "ai"

urlpatterns = [
    path("api/chat/", chat_api, name="chat_api"),
]
