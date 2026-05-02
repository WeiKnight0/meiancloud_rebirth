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

应用层细节见[应用模块](../modules/index.zh-cn.md)，完整路由清单见[URL 参考](../reference/urls.zh-cn.md)。高层职责如下：

| 应用 | 职责 |
|---|---|
| `core` | 公共内容页面、共享模板上下文、错误页、SEO 文件 |
| `accounts` | 注册、登录/登出、资料、头像上传、账号生命周期、管理员初始化命令 |
| `community` | 讨论页、评论 API、层级回复、审核流程 |
| `mysite` | 配置、根路由、WSGI/ASGI 入口 |

## 项目配置

`mysite` 包含项目级配置：

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
