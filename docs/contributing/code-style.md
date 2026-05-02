# Code Style Guide

[简体中文](code-style.zh-cn.md) | [English](#)

## Python

### General

- Follow [PEP 8](https://peps.python.org/pep-0008/)
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 120 characters

### Naming Conventions

| Element | Convention | Example |
|---|---|---|
| Functions | `snake_case` | `user_profile_view` |
| Variables | `snake_case` | `user_profile` |
| Classes | `PascalCase` | `UserProfileForm` |
| Constants | `UPPER_SNAKE_CASE` | `ALLOWED_CONTENT_TYPES` |
| Template tags | `snake_case` | `default_context` |

### Views

- Use function-based views (the project does not use class-based views)
- Always type-hint the `request` parameter: `request: HttpRequest`
- Add a one-line comment at the top of complex views explaining the purpose
- Use `@login_required` and `@require_POST` decorators where appropriate

### Models

- Field names use `snake_case`
- Use `verbose_name` for human-readable field labels
- Add docstrings to model classes
- Keep `related_name` explicit on ForeignKey fields

### Forms

- Inherit from `forms.Form` (not `ModelForm`)
- Use `clean_<fieldname>()` methods for field validation
- Pop custom kwargs in `__init__` with `kwargs.pop()`

## Templates

### Indentation

- Use 4 spaces for indentation
- Keep consistent with existing templates

### Template Tags

- Use `{% extends 'base.html' %}` at the top of every page template
- Use `{% block content %}` for main content
- Use `{% block script %}` for page-specific JavaScript
- Use `{% static 'path' %}` for static file URLs
- Use `{% url 'namespace:name' %}` for URL references

### HTML

- Use semantic HTML where possible
- Keep inline styles minimal — prefer CSS classes
- Add `alt` attributes to all `<img>` tags

## JavaScript

### General

- Use `const` and `let` (no `var`)
- Use modern ES6+ syntax
- Keep scripts in `{% block script %}` or separate `.js` files under `static/`

### AJAX

- Include CSRF token via `X-CSRFToken` header
- Use `FormData` for form submissions
- Handle both success and error responses

## Git

See [Contributing Guide](guide.md) for branch naming, commit message, and PR process conventions.

## Comments

- Add docstrings to public functions and classes
- Use inline comments to explain "why", not "what"
- Keep comments in Chinese or English consistently within a file
