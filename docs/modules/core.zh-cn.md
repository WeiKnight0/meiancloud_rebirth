# 模块：core

[English](core.md) | [简体中文](#)

## 用途

`core` 应用负责所有公共内容页面的渲染，并为整个站点提供共享模板上下文。

## 职责

- 渲染静态内容页面（首页、关于我们、常见问题等）
- 提供 `default_context()` 向每个模板注入用户信息
- 处理自定义错误页面（404、403、500）
- 提供 SEO 文件（sitemap.xml、BingSiteAuth.xml）

## 视图

| 视图 | URL | 方法 | 说明 |
|---|---|---|---|
| `index` | `/` | GET | 首页，含 Swiper 轮播和站点介绍 |
| `findmeian` | `/findmeian/` | GET | 展陈浏览页 |
| `about` | `/about/` | GET | 团队与项目背景 |
| `question_view` | `/question/` | GET | 常见问题，支持展开/折叠 |
| `user_agreement` | `/agreement/` | GET | 用户协议 |
| `login_prompt_view` | `/login_prompt/` | GET | 未登录用户跳转提示页 |

所有视图都是简单的渲染函数，调用 `default_context(request)` 后传入模板。

## 共享上下文

`context.py` 中的 `default_context()` 为每个模板提供：

```python
{
    "nick_name": str | None,    # 导航栏显示名
    "user": User | AnonymousUser,  # 当前 Django 认证用户
    "userprofile": UserProfile | None,  # 当前用户资料（匿名/超管时为 None）
}
```

- **普通用户**：`nick_name` 为其 `UserProfile.nick_name`
- **超级管理员**：`nick_name` 为其 `User.username`
- **匿名用户**：`nick_name` 为 `None`，`userprofile` 为 `None`

## 错误处理器

| 处理器 | 状态码 | 模板 |
|---|---|---|
| `page_not_found` | 404 | `core/errors/404.html` |
| `permission_denied` | 403 | `core/errors/403.html` |
| `server_error` | 500 | `core/errors/500.html` |

## 模板

模板通过 `{% extends 'core/base.html' %}` 继承统一布局。基础模板提供：
- 根据登录状态和管理员身份显示不同链接的导航栏
- 带外部链接的页脚
- 页面切换的淡入淡出动画
- 登出确认弹窗
