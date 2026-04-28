from django.urls import path
from django.views.generic.base import TemplateView

from . import views


app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("findmeian/", views.findmeian, name="findmeian"),
    path("about/", views.about, name="about"),
    path("question/", views.question_view, name="question"),
    path("login_prompt/", views.login_prompt_view, name="login_prompt"),
    path("agreement/", views.user_agreement, name="user-agreement"),
    path(
        "BingSiteAuth.xml",
        TemplateView.as_view(
            template_name="xml/BingSiteAuth.xml", content_type="text/xml"
        ),
    ),
    path(
        "sitemap.xml",
        TemplateView.as_view(template_name="xml/sitemap.xml", content_type="text/xml"),
    ),
]
