# Architecture Overview

[简体中文](overview.zh-cn.md) | [English](#)

## System Architecture

Meian Cloud uses a classic Django monolith structure. Each Django app handles a distinct domain:

```
meiancloud/
├── core/          # Public content pages (homepage, about, FAQ)
├── accounts/      # User registration, login, profile management
├── community/     # Discussion area, comments, moderation
└── mysite/        # Project settings, root URL config, WSGI/ASGI
```

## Request Flow

### Development Mode

```
Browser
  → Django (runserver)
  → SQLite or MySQL
```

### Production Mode (Docker)

```
Browser
  → Nginx (port 80)
    → static files (served directly)
    → media files (served directly)
    → Django/Gunicorn (port 8000)
      → SQLite or MySQL
```

Nginx acts as a reverse proxy, handling static and media file serving directly while forwarding dynamic requests to Gunicorn.

## Application Structure

### `core`

The public-facing content app. Handles:

- **Homepage** (`/`) — Swiper image carousel, site introduction
- **Tracing Meian** (`/findmeian/`) — Exhibition browsing
- **About Us** (`/about/`) — Team and project background
- **FAQ** (`/question/`) — Common questions and answers
- **User Agreement** (`/agreement/`) — Terms of service
- **Login Prompt** (`/login_prompt/`) — Redirect page for unauthenticated users

Also provides shared template context via `default_context()` which injects the current user, profile, and nickname into every template.

### `accounts`

User identity and profile management:

- **Registration** (`/register/`) — Creates `User` + `UserProfile`
- **Login** (`/login/`) — Session-based authentication
- **Logout** (`/logout/`) — POST-only session termination
- **Profile** (`/profile/<userid>/`) — View profile (private fields visible to owner only)
- **Edit Profile** (`/editprofile/<userid>/`) — Update nickname, gender, birthday, avatar, signature
- **Change Password** (`/changepsw/<userid>/`) — Requires old password verification
- **Delete Account** (`/delete_account/`) — POST with password re-verification

Includes `ensure_admin_user` management command for auto-creating/updating admin accounts from environment variables.

### `community`

Discussion and moderation system:

- **Discussion Page** (`/freetotalk/`) — Public comment list with pagination
- **Comment API** (`/api/comments/`) — POST to create top-level comments
- **Reply API** (`/api/comments/<id>/replies/`) — POST to create replies
- **Delete API** (`/api/comments/<id>/`) — DELETE to remove own comments
- **Moderation** (`/comment-management/`) — Superuser-only approve/delete interface

Comments go through an approval workflow (`is_checked` field) before becoming publicly visible.

### `mysite`

Project-level configuration:

- `settings.py` — Django settings, environment variable loading
- `urls.py` — Root URL router, mounts all app URLs
- `wsgi.py` / `asgi.py` — Application entry points

## Key Design Decisions

| Decision | Rationale |
|---|---|
| SQLite by default, MySQL optional | Zero-config local development; MySQL for production |
| Single `Comment` model for comments and replies | Simpler schema; `parent_comment` self-referencing FK enables threading |
| Approval-based comment visibility | Moderation workflow before public display |
| Environment variables for secrets | No hardcoded credentials in source code |
| POST-only logout | Prevents CSRF-based forced logout via GET |
