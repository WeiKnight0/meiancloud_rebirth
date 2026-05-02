# Application Modules

[简体中文](index.zh-cn.md) | [English](#)

This page is the single overview for Meian Cloud's Django apps. For the complete route list, see [URL Reference](../reference/urls.md). For model fields and relationships, see [Data Models](../architecture/data-models.md).

## `core`

The `core` app handles public content pages and shared template context.

Responsibilities:

- Render public pages such as homepage, Tracing Meian, About, FAQ, agreement, and login prompt
- Provide `default_context()` with the current user, profile, and display name for templates
- Handle custom error pages for 404, 403, and 500 responses
- Serve SEO files such as `sitemap.xml` and `BingSiteAuth.xml`

`default_context()` provides:

```python
{
    "nick_name": str | None,
    "user": User | AnonymousUser,
    "userprofile": UserProfile | None,
}
```

Regular users use `UserProfile.nick_name`, superusers use `User.username`, and anonymous users get no profile context.

## `accounts`

The `accounts` app manages the full user lifecycle.

Responsibilities:

- Register users and create `UserProfile` records in one transaction
- Authenticate users with Django sessions and POST-only logout
- Show public/private profile fields based on the viewer
- Edit profiles with avatar upload validation and old-avatar cleanup
- Change passwords with old-password verification
- Delete accounts after password re-confirmation
- Create or update the admin account through `ensure_admin_user`

Profile privacy:

- Owners can see all profile fields
- Other users and superusers only see public fields such as nickname and gender

Avatar uploads accept JPG, PNG, GIF, and WebP files up to 2 MB. Uploaded avatars are stored under `media/accounts/user_img/<user_id>/`, with `static/accounts/img/default.png` used as the fallback.

## `community`

The `community` app provides the public discussion area, threaded comments, JSON APIs, and moderation workflow.

Responsibilities:

- Render the public discussion page with paginated approved comments
- Create top-level comments and replies through AJAX APIs
- Delete comments by owner or superuser
- Require superuser approval before comments become publicly visible
- Use `Prefetch` to avoid N+1 queries when loading approved replies

Comment workflow:

```text
User creates comment
  -> is_checked = False
  -> Superuser reviews it
  -> Approve: is_checked = True and visible publicly
  -> Delete: comment and replies are removed
```

API endpoints return a unified JSON shape:

```json
{"success": true}
```

```json
{"success": false, "error": "error message"}
```
