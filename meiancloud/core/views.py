from django.http import HttpRequest
from django.shortcuts import render

from .context import default_context


def index(request: HttpRequest):
    return render(request, "core/index.html", default_context(request))


def findmeian(request: HttpRequest):
    return render(request, "core/findmeian.html", default_context(request))


def about(request: HttpRequest):
    return render(request, "core/about.html", default_context(request))


def question_view(request: HttpRequest):
    return render(request, "core/question.html", default_context(request))


def user_agreement(request: HttpRequest):
    return render(request, "core/user-agreement.html", default_context(request))


def login_prompt_view(request: HttpRequest):
    return render(request, "core/login_prompt.html", context=default_context(request))
