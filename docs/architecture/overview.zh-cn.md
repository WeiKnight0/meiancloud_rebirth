# 系统架构

[English](overview.md) | [简体中文](#)

## 系统架构

梅庵云迹采用典型的 Django 单体应用结构。每个 Django app 负责一个独立的业务领域：

```
meiancloud/
├── core/          # 公共内容页面（首页、关于我们、常见问题）
├── accounts/      # 用户注册、登录、个人资料管理
├── community/     # 评论区、讨论、审核管理
└── mysite/        # 项目配置、根路由、WSGI/ASGI 入口
```

## 请求链路

### 开发模式

```
浏览器
  → Django (runserver)
  → SQLite 或 MySQL
```

### 生产模式（Docker）

```
浏览器
  → Nginx (端口 80)
    → 静态文件（直接返回）
    → 媒体文件（直接返回）
    → Django/Gunicorn (端口 8000)
      → SQLite 或 MySQL
```

Nginx 作为反向代理，直接处理静态文件和媒体文件请求，动态请求转发给 Gunicorn。

## 应用结构

### `core`

公共内容页面应用，负责：

- **首页** (`/`) — Swiper 图片轮播、网站介绍
- **循迹梅庵** (`/findmeian/`) — 展陈浏览
- **关于我们** (`/about/`) — 团队与项目背景
- **常见问题** (`/question/`) — 高频问题解答
- **用户协议** (`/agreement/`) — 使用条款
- **登录提示** (`/login_prompt/`) — 未登录用户的跳转页

同时通过 `default_context()` 提供共享模板上下文，将当前用户、用户资料和昵称注入到每个模板中。

### `accounts`

用户身份与资料管理：

- **注册** (`/register/`) — 同时创建 `User` 和 `UserProfile`
- **登录** (`/login/`) — 基于 Session 的认证
- **登出** (`/logout/`) — 仅限 POST 的会话终止
- **个人主页** (`/profile/<userid>/`) — 查看资料（私密字段仅本人可见）
- **编辑资料** (`/editprofile/<userid>/`) — 修改昵称、性别、生日、头像、签名
- **修改密码** (`/changepsw/<userid>/`) — 需验证旧密码
- **注销账号** (`/delete_account/`) — POST 并重新输入密码确认

包含 `ensure_admin_user` 管理命令，可从环境变量自动创建或更新管理员账号。

### `community`

讨论与审核系统：

- **讨论页** (`/freetotalk/`) — 公开评论列表，支持分页
- **评论接口** (`/api/comments/`) — POST 创建顶级评论
- **回复接口** (`/api/comments/<id>/replies/`) — POST 创建回复
- **删除接口** (`/api/comments/<id>/`) — DELETE 删除自己的评论
- **审核管理** (`/comment-management/`) — 超级管理员审核/删除

评论采用审核制（`is_checked` 字段），发布后需管理员审核才对外可见。

### `mysite`

项目级配置：

- `settings.py` — Django 配置、环境变量加载
- `urls.py` — 根路由，挂载所有 app 路由
- `wsgi.py` / `asgi.py` — 应用入口

## 关键设计决策

| 决策 | 原因 |
|---|---|
| 默认 SQLite，可选 MySQL | 本地开发零配置；生产环境使用 MySQL |
| 评论和回复使用单一 `Comment` 模型 | 数据结构更简洁；`parent_comment` 自关联实现层级 |
| 评论审核制 | 公开显示前需管理员审核 |
| 环境变量管理密钥 | 源码中不硬编码任何凭据 |
| 登出仅限 POST | 防止通过 GET 触发 CSRF 强制登出 |
