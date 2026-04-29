# Data Models

[简体中文](data-models.zh-cn.md) | [English](#)

## Entity Relationship

```
User (Django built-in)
  └── 1:1 ── UserProfile
                 └── 1:N ── Comment
                              └── self-referencing (parent_comment)
```

## `UserProfile`

Extends Django's built-in `User` model with additional profile fields.

| Field | Type | Constraints | Description |
|---|---|---|---|
| `owner` | `OneToOneField(User)` | `on_delete=CASCADE` | Link to auth user |
| `nick_name` | `CharField(max_length=20)` | `blank=True, default=""` | Display name |
| `gender` | `CharField(max_length=8)` | choices: `0`(default), `male`, `female`, `others` | Gender selection |
| `birthday` | `DateField` | `null=True, blank=True` | Date of birth |
| `image` | `ImageField` | `upload_to=user_directory_path, null=True, blank=True` | Avatar |
| `sign` | `TextField(max_length=100)` | `null=True, blank=True, default=""` | Personal signature |

### Avatar Storage

Avatars are stored at `media/accounts/user_img/<user_id>/<user_id>.<ext>`. Each user's avatar is named by their user ID, so uploading a new avatar overwrites the old file.

The `save()` method automatically deletes the previous avatar file when a new one is uploaded.

The `avatar_url` property returns the image URL if an avatar exists, otherwise falls back to `static/accounts/img/default.png`.

## `Comment`

A single model handles both top-level comments and replies through self-referencing.

| Field | Type | Constraints | Description |
|---|---|---|---|
| `owner` | `ForeignKey(UserProfile)` | `on_delete=CASCADE, related_name="comments"` | Comment author |
| `title` | `TextField(max_length=50)` | `blank=True, null=True` | Comment title (null for replies) |
| `content` | `TextField(max_length=200)` | Required | Comment body |
| `date` | `DateTimeField` | `auto_now_add=True` | Creation timestamp |
| `parent_comment` | `ForeignKey("self")` | `on_delete=CASCADE, null=True, blank=True, related_name="replies"` | Parent comment (null = top-level) |
| `is_checked` | `BooleanField` | `default=False` | Moderation approval status |

### Comment Threading

- **Top-level comment**: `parent_comment` is `null`, `title` is set
- **Reply**: `parent_comment` points to the parent, `title` is `null`

When a top-level comment is deleted, all its replies are cascade-deleted via `on_delete=CASCADE`.

### Moderation Workflow

1. User creates a comment → `is_checked = False` (not publicly visible)
2. Superuser reviews in `/comment-management/`
3. Approve → `is_checked = True` (visible on discussion page)
4. Delete → comment and its replies are removed
