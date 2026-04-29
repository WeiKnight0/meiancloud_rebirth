# Module: accounts

[简体中文](accounts.zh-cn.md) | [English](#)

## Purpose

The `accounts` app manages the full user lifecycle: registration, authentication, profile management, and account deletion.

## Responsibilities

- User registration (creates both `User` and `UserProfile`)
- Session-based login and POST-only logout
- Profile viewing with privacy controls
- Profile editing with avatar upload and server-side validation
- Password change with old password verification
- Account deletion with password re-confirmation

## Views

| View | URL | Method | Auth Required | Description |
|---|---|---|---|---|
| `login_view` | `/login/` | GET/POST | No | Login form and authentication |
| `register_view` | `/register/` | GET/POST | No | Registration form, auto-login on success |
| `logout_view` | `/logout/` | POST | No | Session termination |
| `user_profile_view` | `/profile/<userid>/` | GET | No | View profile (private fields owner-only) |
| `changepsw_view` | `/changepsw/<userid>/` | GET/POST | Yes (owner) | Change password |
| `editprofile_view` | `/editprofile/<userid>/` | GET/POST | Yes (owner) | Edit profile and avatar |
| `delete_account` | `/delete_account/` | POST | Yes | Delete account with password check |

## Registration Flow

1. User fills in username, password, email, nickname, gender, birthday
2. Form validates: unique username, password match, gender selection
3. `User.objects.create_user()` + `UserProfile.objects.create()` inside `transaction.atomic()`
4. On `IntegrityError`, form shows "username already exists"
5. On success, user is automatically logged in

## Privacy Model

Profile visibility depends on the viewer:
- **Owner**: sees all fields (email, birthday, signature, gender, nickname)
- **Other users**: sees only nickname and gender
- **Superusers**: sees only nickname and gender (same as other users)

The `show_private` template flag controls this.

## Avatar Upload

- **Server-side validation**: content type must be JPG/PNG/GIF/WebP, max 2MB
- **Storage**: `media/accounts/user_img/<user_id>/<user_id>.<ext>`
- **Cleanup**: old avatar is automatically deleted when a new one is uploaded (handled in `UserProfile.save()`)
- **Fallback**: `static/accounts/img/default.png` when no avatar is set

## Management Command

### `ensure_admin_user`

Creates or updates a default admin account from environment variables.

```bash
python manage.py ensure_admin_user
```

Reads from:
- `ADMIN_USERNAME` (default: `admin`)
- `ADMIN_PASSWORD` (required, no default)
- `ADMIN_EMAIL` (default: `admin@example.com`)

Always sets `is_staff=True` and `is_superuser=True`. Runs on every Docker startup.
