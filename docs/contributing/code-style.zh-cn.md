# 代码风格指南

[English](code-style.md) | [简体中文](#)

## Python

### 通用规范

- 遵循 [PEP 8](https://peps.python.org/pep-0008/)
- 使用 4 空格缩进（不用 Tab）
- 最大行宽：120 字符

### 命名规范

| 元素 | 规范 | 示例 |
|---|---|---|
| 函数 | `snake_case` | `user_profile_view` |
| 变量 | `snake_case` | `user_profile` |
| 类 | `PascalCase` | `UserProfileForm` |
| 常量 | `UPPER_SNAKE_CASE` | `ALLOWED_CONTENT_TYPES` |
| 模板标签 | `snake_case` | `default_context` |

### 视图

- 使用函数视图（项目不使用类视图）
- 始终对 `request` 参数添加类型标注：`request: HttpRequest`
- 复杂视图顶部添加单行注释说明用途
- 适当使用 `@login_required` 和 `@require_POST` 装饰器

### 模型

- 字段名使用 `snake_case`
- 使用 `verbose_name` 提供人类可读标签
- 模型类添加文档字符串
- ForeignKey 字段显式设置 `related_name`

### 表单

- 继承 `forms.Form`（不使用 `ModelForm`）
- 使用 `clean_<fieldname>()` 方法进行字段验证
- `__init__` 中通过 `kwargs.pop()` 弹出自定义参数

## 模板

### 缩进

- 使用 4 空格缩进
- 保持与现有模板一致

### 模板标签

- 每个页面模板顶部使用 `{% extends 'base.html' %}`
- 主内容使用 `{% block content %}`
- 页面特定 JavaScript 使用 `{% block script %}`
- 静态文件使用 `{% static 'path' %}`
- URL 引用使用 `{% url 'namespace:name' %}`

### HTML

- 尽量使用语义化 HTML
- 减少内联样式 — 优先使用 CSS 类
- 所有 `<img>` 标签添加 `alt` 属性

## JavaScript

### 通用规范

- 使用 `const` 和 `let`（不用 `var`）
- 使用现代 ES6+ 语法
- 脚本放在 `{% block script %}` 或 `static/` 下的独立 `.js` 文件中

### AJAX

- 通过 `X-CSRFToken` 头部携带 CSRF 令牌
- 表单提交使用 `FormData`
- 同时处理成功和错误响应

## Git

分支命名、提交信息和 PR 流程规范见[贡献指南](guide.zh-cn.md)。

## 注释

- 公共函数和类添加文档字符串
- 行内注释解释"为什么"而非"做什么"
- 同一文件内注释语言保持一致（中文或英文）
