from django.http import HttpRequest
from django.shortcuts import render

from .context import default_context


def index(request: HttpRequest):
    return render(request, "home/index.html", default_context(request))


def findmeian(request: HttpRequest):
    return render(request, "home/findmeian.html", default_context(request))


def about(request: HttpRequest):
    return render(request, "home/about.html", default_context(request))


def question_view(request: HttpRequest):
    return render(request, "home/question.html", default_context(request))


def user_agreement(request: HttpRequest):
    return render(request, "home/user-agreement.html", default_context(request))


def login_prompt_view(request: HttpRequest):
    return render(request, "home/login_prompt.html", context=default_context(request))
