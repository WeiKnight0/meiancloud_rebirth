# 应用模块

[English](index.md) | [简体中文](#)

本文是梅庵云迹 Django 应用的统一总览。完整路由清单见[URL 参考](../reference/urls.zh-cn.md)，模型字段与关系见[数据模型](../architecture/data-models.zh-cn.md)。

## `core`

`core` 应用负责公共内容页面和共享模板上下文。

职责：

- 渲染首页、循迹梅庵、关于我们、常见问题、用户协议、登录提示等公共页面
- 通过 `default_context()` 为模板提供当前用户、用户资料和显示名
- 处理 404、403、500 自定义错误页
- 提供 `sitemap.xml` 和 `BingSiteAuth.xml` 等 SEO 文件

`default_context()` 提供：

```python
{
    "nick_name": str | None,
    "user": User | AnonymousUser,
    "userprofile": UserProfile | None,
}
```

普通用户使用 `UserProfile.nick_name`，超级管理员使用 `User.username`，匿名用户没有资料上下文。

## `accounts`

`accounts` 应用管理完整的用户生命周期。

职责：

- 在同一事务中注册用户并创建 `UserProfile`
- 使用 Django Session 认证，并限制登出只能通过 POST
- 根据访问者身份展示公开或私密资料字段
- 编辑资料，支持头像上传校验和旧头像清理
- 修改密码时校验旧密码
- 注销账号时重新校验密码
- 通过 `ensure_admin_user` 创建或更新管理员账号

资料隐私：

- 本人可以查看全部资料字段
- 其他用户和超级管理员只能查看昵称、性别等公开字段

头像上传支持 JPG、PNG、GIF、WebP，最大 2 MB。上传文件存储在 `media/accounts/user_img/<user_id>/`，未设置头像时使用 `static/accounts/img/default.png`。

## `community`

`community` 应用提供公开讨论区、层级评论、JSON API 和审核流程。

职责：

- 渲染公开讨论页，分页展示已审核评论
- 通过 AJAX API 创建顶级评论和回复
- 允许作者或超级管理员删除评论
- 评论公开展示前必须由超级管理员审核
- 使用 `Prefetch` 加载已审核回复，避免 N+1 查询

评论流程：

```text
用户创建评论
  -> is_checked = False
  -> 超级管理员审核
  -> 通过：is_checked = True 并公开可见
  -> 删除：评论及其回复一并移除
```

API 统一返回：

```json
{"success": true}
```

```json
{"success": false, "error": "错误信息"}
```
