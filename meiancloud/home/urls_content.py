from django.urls import path
from django.views.generic.base import TemplateView

from . import views_content


urlpatterns = [
    path("", views_content.index, name="index"),
    path("findmeian/", views_content.findmeian, name="findmeian"),
    path("about/", views_content.about, name="about"),
    path("question/", views_content.question_view, name="question"),
    path("login_prompt/", views_content.login_prompt_view, name="login_prompt"),
    path("agreement/", views_content.user_agreement, name="user-agreement"),
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
