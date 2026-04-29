# 模块：accounts

[English](accounts.md) | [简体中文](#)

## 用途

`accounts` 应用管理完整的用户生命周期：注册、认证、资料管理和账号注销。

## 职责

- 用户注册（同时创建 `User` 和 `UserProfile`）
- 基于 Session 的登录和仅限 POST 的登出
- 带隐私控制的个人主页
- 资料编辑，含头像上传和服务端校验
- 修改密码（需验证旧密码）
- 注销账号（需重新输入密码确认）

## 视图

| 视图 | URL | 方法 | 需登录 | 说明 |
|---|---|---|---|---|
| `login_view` | `/login/` | GET/POST | 否 | 登录表单和认证 |
| `register_view` | `/register/` | GET/POST | 否 | 注册表单，成功后自动登录 |
| `logout_view` | `/logout/` | POST | 否 | 终止会话 |
| `user_profile_view` | `/profile/<userid>/` | GET | 否 | 查看资料（私密字段仅本人可见） |
| `changepsw_view` | `/changepsw/<userid>/` | GET/POST | 是（本人） | 修改密码 |
| `editprofile_view` | `/editprofile/<userid>/` | GET/POST | 是（本人） | 编辑资料和头像 |
| `delete_account` | `/delete_account/` | POST | 是 | 注销账号，需密码确认 |

## 注册流程

1. 用户填写用户名、密码、邮箱、昵称、性别、生日
2. 表单校验：用户名唯一、密码一致、性别必选
3. `transaction.atomic()` 内执行 `User.objects.create_user()` + `UserProfile.objects.create()`
4. `IntegrityError` 时表单显示"用户名已存在"
5. 成功后自动登录

## 隐私模型

个人主页的可见性取决于查看者：
- **本人**：可见所有字段（邮箱、生日、签名、性别、昵称）
- **其他用户**：仅可见昵称和性别
- **超级管理员**：仅可见昵称和性别

模板中通过 `show_private` 标志控制。

## 头像上传

- **服务端校验**：文件类型限 JPG/PNG/GIF/WebP，大小限 2MB
- **存储路径**：`media/accounts/user_img/<user_id>/<user_id>.<ext>`
- **自动清理**：上传新头像时自动删除旧文件（由 `UserProfile.save()` 处理）
- **默认头像**：未设置头像时使用 `static/accounts/img/default.png`

## 管理命令

### `ensure_admin_user`

从环境变量自动创建或更新管理员账号。

```bash
python manage.py ensure_admin_user
```

读取环境变量：
- `ADMIN_USERNAME`（默认：`admin`）
- `ADMIN_PASSWORD`（必填，无默认值）
- `ADMIN_EMAIL`（默认：`admin@example.com`）

始终设置 `is_staff=True` 和 `is_superuser=True`。Docker 启动时每次执行。
