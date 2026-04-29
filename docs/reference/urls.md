# URL Reference

[简体中文](urls.zh-cn.md) | [English](#)

Complete list of all URL patterns in the project.

## Root URLs (`mysite/urls.py`)

All app URLs are mounted at the root level.

| Pattern | Includes | Namespace |
|---|---|---|
| `admin/` | Django admin | — |
| `''` | `core.urls` | `core` |
| `''` | `accounts.urls` | `accounts` |
| `''` | `community.urls` | `community` |

## core URLs

| URL Pattern | View | Name | Method | Description |
|---|---|---|---|---|
| `/` | `index` | `core:index` | GET | Homepage |
| `/findmeian/` | `findmeian` | `core:findmeian` | GET | Exhibition browsing |
| `/about/` | `about` | `core:about` | GET | About us |
| `/question/` | `question_view` | `core:question` | GET | FAQ |
| `/login_prompt/` | `login_prompt_view` | `core:login_prompt` | GET | Login prompt redirect |
| `/agreement/` | `user_agreement` | `core:user-agreement` | GET | User agreement |
| `/BingSiteAuth.xml` | `TemplateView` | — | GET | Bing verification |
| `/sitemap.xml` | `TemplateView` | — | GET | SEO sitemap |

## accounts URLs

| URL Pattern | View | Name | Method | Auth | Description |
|---|---|---|---|---|---|
| `/login/` | `login_view` | `accounts:login` | GET/POST | No | Login |
| `/register/` | `register_view` | `accounts:register` | GET/POST | No | Registration |
| `/logout/` | `logout_view` | `accounts:logout` | POST | No | Logout |
| `/profile/<int:userid>/` | `user_profile_view` | `accounts:userprofile` | GET | No | View profile |
| `/changepsw/<int:userid>/` | `changepsw_view` | `accounts:changepsw` | GET/POST | Yes | Change password |
| `/editprofile/<int:userid>/` | `editprofile_view` | `accounts:editprofile` | GET/POST | Yes | Edit profile |
| `/delete_account/` | `delete_account` | `accounts:delete_account` | POST | Yes | Delete account |

## community URLs

| URL Pattern | View | Name | Method | Auth | Description |
|---|---|---|---|---|---|
| `/freetotalk/` | `freetotalk_page` | `community:freetotalk` | GET | No | Discussion page |
| `/api/comments/` | `comment_create` | `community:comment_create` | POST | Yes | Create comment |
| `/api/comments/<int:comment_id>/` | `comment_delete` | `community:comment_delete` | DELETE | Yes | Delete comment |
| `/api/comments/<int:comment_id>/replies/` | `reply_create` | `community:reply_create` | POST | Yes | Create reply |
| `/comment-management/` | `comment_management` | `community:comment-management` | GET/POST | Superuser | Moderation |
