# URL 路由参考

[English](urls.md) | [简体中文](#)

项目中所有 URL 路由的完整列表。

## 根路由（`mysite/urls.py`）

所有 app 路由挂载在根路径下。

| 模式 | 包含 | 命名空间 |
|---|---|---|
| `admin/` | Django admin | — |
| `''` | `core.urls` | `core` |
| `''` | `accounts.urls` | `accounts` |
| `''` | `community.urls` | `community` |

## core 路由

| URL 模式 | 视图 | 名称 | 方法 | 说明 |
|---|---|---|---|---|
| `/` | `index` | `core:index` | GET | 首页 |
| `/findmeian/` | `findmeian` | `core:findmeian` | GET | 展陈浏览 |
| `/about/` | `about` | `core:about` | GET | 关于我们 |
| `/question/` | `question_view` | `core:question` | GET | 常见问题 |
| `/login_prompt/` | `login_prompt_view` | `core:login_prompt` | GET | 登录提示跳转 |
| `/agreement/` | `user_agreement` | `core:user-agreement` | GET | 用户协议 |
| `/BingSiteAuth.xml` | `TemplateView` | — | GET | Bing 验证文件 |
| `/sitemap.xml` | `TemplateView` | — | GET | SEO 站点地图 |

## accounts 路由

| URL 模式 | 视图 | 名称 | 方法 | 需登录 | 说明 |
|---|---|---|---|---|---|
| `/login/` | `login_view` | `accounts:login` | GET/POST | 否 | 登录 |
| `/register/` | `register_view` | `accounts:register` | GET/POST | 否 | 注册 |
| `/logout/` | `logout_view` | `accounts:logout` | POST | 否 | 登出 |
| `/profile/<int:userid>/` | `user_profile_view` | `accounts:userprofile` | GET | 否 | 查看资料 |
| `/changepsw/<int:userid>/` | `changepsw_view` | `accounts:changepsw` | GET/POST | 是 | 修改密码 |
| `/editprofile/<int:userid>/` | `editprofile_view` | `accounts:editprofile` | GET/POST | 是 | 编辑资料 |
| `/delete_account/` | `delete_account` | `accounts:delete_account` | POST | 是 | 注销账号 |

## community 路由

| URL 模式 | 视图 | 名称 | 方法 | 需登录 | 说明 |
|---|---|---|---|---|---|
| `/freetotalk/` | `freetotalk_page` | `community:freetotalk` | GET | 否 | 讨论页 |
| `/api/comments/` | `comment_create` | `community:comment_create` | POST | 是 | 创建评论 |
| `/api/comments/<int:comment_id>/` | `comment_delete` | `community:comment_delete` | DELETE | 是 | 删除评论 |
| `/api/comments/<int:comment_id>/replies/` | `reply_create` | `community:reply_create` | POST | 是 | 创建回复 |
| `/comment-management/` | `comment_management` | `community:comment-management` | GET/POST | 超级管理员 | 审核管理 |
