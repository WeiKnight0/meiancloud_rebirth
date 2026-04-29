# Module: core

[简体中文](core.zh-cn.md) | [English](#)

## Purpose

The `core` app handles all public-facing content pages and provides shared template context for the entire site.

## Responsibilities

- Renders static content pages (homepage, about, FAQ, etc.)
- Provides `default_context()` that injects user info into every template
- Handles custom error pages (404, 403, 500)
- Serves SEO files (sitemap.xml, BingSiteAuth.xml)

## Views

| View | URL | Method | Description |
|---|---|---|---|
| `index` | `/` | GET | Homepage with Swiper carousel and site intro |
| `findmeian` | `/findmeian/` | GET | Exhibition browsing page |
| `about` | `/about/` | GET | Team and project background |
| `question_view` | `/question/` | GET | FAQ with expandable Q&A items |
| `user_agreement` | `/agreement/` | GET | Terms of service |
| `login_prompt_view` | `/login_prompt/` | GET | Redirect page for unauthenticated users |

All views are simple render-only functions. They call `default_context(request)` and pass it to the template.

## Shared Context

`default_context()` in `context.py` provides every template with:

```python
{
    "nick_name": str | None,    # Display name for navigation bar
    "user": User | AnonymousUser,  # Current Django auth user
    "userprofile": UserProfile | None,  # Current user's profile (None for anon/superuser)
}
```

- **Regular users**: `nick_name` is their `UserProfile.nick_name`
- **Superusers**: `nick_name` is their `User.username`
- **Anonymous**: `nick_name` is `None`, `userprofile` is `None`

## Error Handlers

| Handler | Status | Template |
|---|---|---|
| `page_not_found` | 404 | `core/errors/404.html` |
| `permission_denied` | 403 | `core/errors/403.html` |
| `server_error` | 500 | `core/errors/500.html` |

## Templates

Templates use `{% extends 'core/base.html' %}` for consistent layout. The base template provides:
- Navigation bar with conditional links based on auth/superuser status
- Footer with external links
- Fade-in/out page transition animation
- Logout confirmation dialog
