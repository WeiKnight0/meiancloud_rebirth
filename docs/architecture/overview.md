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

The app-level details live in [Application Modules](../modules/index.md), and the complete route list lives in [URL Reference](../reference/urls.md). At a high level:

| App | Responsibility |
|---|---|
| `core` | Public content pages, shared template context, error pages, SEO files |
| `accounts` | Registration, login/logout, profiles, avatar upload, account lifecycle, admin bootstrap command |
| `community` | Discussion page, comment APIs, threaded replies, moderation workflow |
| `mysite` | Settings, root URL routing, WSGI/ASGI entry points |

## Project Configuration

`mysite` contains project-level configuration:

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
