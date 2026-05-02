# 贡献指南

[English](guide.md) | [简体中文](#)

感谢你对梅庵云迹项目的关注！

## 快速开始

### 1. Fork 并克隆

```bash
# 在 GitHub 上 Fork，然后：
git clone https://github.com/<your-username>/meiancloud_rebirth.git
cd meiancloud_rebirth
```

### 2. 搭建开发环境

使用[快速开始](../getting-started/quickstart.zh-cn.md)中的标准步骤。该文档同时覆盖本地 Python 环境和 Docker 启动方式。

### 3. 创建分支

```bash
git checkout -b feature/your-feature-name
```

## 分支命名

| 前缀 | 用途 | 示例 |
|---|---|---|
| `feature/` | 新功能 | `feature/comment-search` |
| `fix/` | 修复 Bug | `fix/avatar-upload-error` |
| `docs/` | 文档修改 | `docs/update-deployment-guide` |
| `refactor/` | 代码重构 | `refactor/separate-community-views` |

## 进行修改

### 开始之前

1. 检查已有的 Issue 和 PR，避免重复
2. 大型变更建议先开 Issue 讨论方案

### 工作过程中

1. 保持提交原子性 — 每个提交一个逻辑变更
2. 编写清晰的提交信息（见下方）
3. 推送前在本地测试

### 提交信息

使用祈使语气，主题行不超过 72 字符：

```
Add comment search feature

- Add search field to comment list page
- Add filter queryset in freetotalk_page view
- Add pagination for search results
```

好的：`Add avatar upload validation`
不好的：`Fixed stuff` 或 `Update views.py`

## Pull Request 流程

1. 推送分支到你的 Fork
2. 向 `main` 发起 Pull Request
3. 填写 PR 描述：
   - 这个变更做了什么
   - 为什么需要这个变更
   - 如何测试
4. 等待 CI 检查和代码评审
5. 根据评审反馈进行修改

## 代码评审

- 所有 PR 合并前需要至少一次评审
- CI 检查必须通过
- 评审者可能要求修改 — 这是正常的

## 报告问题

报告 Bug 时请包含：
- 复现步骤
- 期望行为
- 实际行为
- Python/Django 版本
- 浏览器（如果是前端问题）

## 许可证

参与贡献即表示你同意你的贡献将采用 MIT 许可证。
