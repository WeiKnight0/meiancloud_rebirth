# 数据模型

[English](data-models.md) | [简体中文](#)

## 实体关系

```
User (Django 内置)
  └── 1:1 ── UserProfile
                 └── 1:N ── Comment
                              └── 自关联 (parent_comment)
```

## `UserProfile`

扩展 Django 内置 `User` 模型，添加用户资料字段。

| 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|
| `owner` | `OneToOneField(User)` | `on_delete=CASCADE` | 关联认证用户 |
| `nick_name` | `CharField(max_length=20)` | `blank=True, default=""` | 显示昵称 |
| `gender` | `CharField(max_length=8)` | 选项：`0`（默认）、`male`、`female`、`others` | 性别 |
| `birthday` | `DateField` | `null=True, blank=True` | 出生日期 |
| `image` | `ImageField` | `upload_to=user_directory_path, null=True, blank=True` | 头像 |
| `sign` | `TextField(max_length=100)` | `null=True, blank=True, default=""` | 个性签名 |

### 头像存储

头像存储路径为 `media/accounts/user_img/<user_id>/<user_id>.<ext>`。每个用户的头像以用户 ID 命名，上传新头像会覆盖旧文件。

`save()` 方法会在上传新头像时自动删除之前的文件。

`avatar_url` 属性在头像存在时返回图片 URL，否则回退到 `static/accounts/img/default.png`。

## `Comment`

单一模型通过自关联同时支持顶级评论和回复。

| 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|
| `owner` | `ForeignKey(UserProfile)` | `on_delete=CASCADE, related_name="comments"` | 评论作者 |
| `title` | `TextField(max_length=50)` | `blank=True, null=True` | 评论标题（回复时为 null） |
| `content` | `TextField(max_length=200)` | 必填 | 评论内容 |
| `date` | `DateTimeField` | `auto_now_add=True` | 创建时间 |
| `parent_comment` | `ForeignKey("self")` | `on_delete=CASCADE, null=True, blank=True, related_name="replies"` | 父评论（null = 顶级评论） |
| `is_checked` | `BooleanField` | `default=False` | 审核状态 |

### 评论层级

- **顶级评论**：`parent_comment` 为 `null`，`title` 有值
- **回复**：`parent_comment` 指向父评论，`title` 为 `null`

删除顶级评论时，其下所有回复通过 `on_delete=CASCADE` 级联删除。

### 审核流程

1. 用户创建评论 → `is_checked = False`（不对外显示）
2. 超级管理员在 `/comment-management/` 审核
3. 通过 → `is_checked = True`（在讨论页可见）
4. 删除 → 评论及其回复一并移除
