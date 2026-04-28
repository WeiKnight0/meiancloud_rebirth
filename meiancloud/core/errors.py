from django.shortcuts import render

from .context import default_context


def page_not_found(request, exception, template_name="core/errors/404.html"):
    return render(request, template_name=template_name, context=default_context(request))


def server_error(request, template_name="core/errors/500.html"):
    return render(request, template_name, context=default_context(request))


def permission_denied(request, template_name="core/errors/403.html"):
    return render(request, template_name, context=default_context(request))
