# Module: community

[简体中文](community.zh-cn.md) | [English](#)

## Purpose

The `community` app provides a discussion area with threaded comments, RESTful APIs, and a superuser moderation workflow.

## Responsibilities

- Public discussion page with paginated comments
- RESTful API for creating, replying to, and deleting comments
- Comment moderation (approve/delete) by superusers
- Threaded replies via self-referencing `Comment` model

## Views

### Page View

| View | URL | Method | Description |
|---|---|---|---|
| `freetotalk_page` | `/freetotalk/` | GET | Discussion page with comments and reply forms |

### API Endpoints

| View | URL | Method | Auth | Description |
|---|---|---|---|---|
| `comment_create` | `/api/comments/` | POST | Yes (non-superuser) | Create a top-level comment |
| `reply_create` | `/api/comments/<id>/replies/` | POST | Yes (non-superuser) | Create a reply to a comment |
| `comment_delete` | `/api/comments/<id>/` | DELETE | Yes (owner or superuser) | Delete a comment and its replies |

### Moderation

| View | URL | Method | Auth | Description |
|---|---|---|---|---|
| `comment_management` | `/comment-management/` | GET/POST | Superuser | Approve or delete comments |

## Comment Workflow

```
User creates comment
  → is_checked = False (not publicly visible)
  → Superuser reviews in /comment-management/
  → Approve: is_checked = True (visible on /freetotalk/)
  → Delete: comment and replies removed
```

## API Response Format

All API endpoints return a unified JSON structure:

```json
// Success
{"success": true}

// Failure
{"success": false, "error": "error message"}
```

### Error Codes

| Status | Meaning |
|---|---|
| 400 | Invalid form data |
| 401 | Not authenticated |
| 403 | Not authorized (not owner or superuser) |
| 405 | Wrong HTTP method |
| 500 | Server error |

## Frontend Integration

The discussion page uses AJAX for all write operations:

- **Comment form** → POST to `/api/comments/`
- **Reply form** → POST to `/api/comments/<id>/replies/`
- **Delete button** → DELETE to `/api/comments/<id>/`

All requests include the CSRF token via the `X-CSRFToken` header.

## Query Optimization

The comment list page uses `Prefetch` to avoid N+1 queries:

```python
Prefetch(
    "replies",
    queryset=Comment.objects.filter(is_checked=True).select_related("owner__owner"),
    to_attr="visible_replies",
)
```

This fetches all approved replies in a single query, stored as `visible_replies` on each comment.
