# 模块：community

[English](community.md) | [简体中文](#)

## 用途

`community` 应用提供带层级回复的讨论区、RESTful API 和超级管理员审核工作流。

## 职责

- 公开讨论页，支持分页浏览
- RESTful API：创建评论、回复、删除
- 评论审核（通过/删除），仅超级管理员可操作
- 通过自关联 `Comment` 模型实现层级回复

## 视图

### 页面视图

| 视图 | URL | 方法 | 说明 |
|---|---|---|---|
| `freetotalk_page` | `/freetotalk/` | GET | 讨论页，含评论列表和回复表单 |

### API 接口

| 视图 | URL | 方法 | 需登录 | 说明 |
|---|---|---|---|---|
| `comment_create` | `/api/comments/` | POST | 是（非管理员） | 创建顶级评论 |
| `reply_create` | `/api/comments/<id>/replies/` | POST | 是（非管理员） | 回复评论 |
| `comment_delete` | `/api/comments/<id>/` | DELETE | 是（作者或管理员） | 删除评论及其回复 |

### 审核管理

| 视图 | URL | 方法 | 需登录 | 说明 |
|---|---|---|---|---|
| `comment_management` | `/comment-management/` | GET/POST | 超级管理员 | 审核通过或删除评论 |

## 评论工作流

```
用户创建评论
  → is_checked = False（不对外显示）
  → 超级管理员在 /comment-management/ 审核
  → 通过：is_checked = True（在 /freetotalk/ 可见）
  → 删除：评论及其回复一并移除
```

## API 响应格式

所有 API 接口统一返回：

```json
// 成功
{"success": true}

// 失败
{"success": false, "error": "错误信息"}
```

### 错误码

| 状态码 | 含义 |
|---|---|
| 400 | 表单数据无效 |
| 401 | 未登录 |
| 403 | 无权操作（非作者/非管理员） |
| 405 | HTTP 方法不允许 |
| 500 | 服务器内部错误 |

## 前端交互

讨论页所有写操作通过 AJAX 完成：

- **评论表单** → POST 到 `/api/comments/`
- **回复表单** → POST 到 `/api/comments/<id>/replies/`
- **删除按钮** → DELETE 到 `/api/comments/<id>/`

所有请求通过 `X-CSRFToken` 头部携带 CSRF 令牌。

## 查询优化

评论列表页使用 `Prefetch` 避免 N+1 查询：

```python
Prefetch(
    "replies",
    queryset=Comment.objects.filter(is_checked=True).select_related("owner__owner"),
    to_attr="visible_replies",
)
```

单次查询获取所有已审核回复，存储在每个评论的 `visible_replies` 属性上。
