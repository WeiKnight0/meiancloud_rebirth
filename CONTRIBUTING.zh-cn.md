# 贡献指南

[English](CONTRIBUTING.md) | [简体中文](#)

感谢你对梅庵云迹项目的关注！本指南说明如何参与贡献。

## 如何贡献

### 1. Fork 仓库

在 GitHub 上点击 "Fork" 按钮，创建自己的副本。

### 2. 克隆你的 Fork

```bash
git clone https://github.com/<your-username>/meiancloud_rebirth.git
cd meiancloud_rebirth
```

### 3. 创建分支

```bash
git checkout -b feature/your-feature-name
```

分支命名规范：
- `feature/xxx` — 新功能
- `fix/xxx` — 修复 Bug
- `docs/xxx` — 仅文档修改

### 4. 进行修改

遵循代码风格规范：
- Python：遵循 PEP 8
- 模板：沿用现有的缩进模式
- 提交信息：使用祈使语气（"Add feature" 而非 "Added feature"）

### 5. 本地测试

```bash
cd meiancloud
cp .env.example .env
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

### 6. 提交并推送

```bash
git add .
git commit -m "添加描述性的提交信息"
git push origin feature/your-feature-name
```

### 7. 发起 Pull Request

在 GitHub 上你的 Fork 仓库中点击 "New Pull Request"。请描述：
- 这个变更做了什么
- 为什么需要这个变更
- 如何测试

## 代码风格

### Python
- 遵循 [PEP 8](https://peps.python.org/pep-0008/)
- 使用有意义的变量和函数名
- 为新函数和类添加文档字符串

### 模板
- 保持现有的缩进风格（4 空格）
- 统一使用 Django 模板标签

### Git
- 保持提交的原子性（每个提交一个逻辑变更）
- 编写清晰的提交信息

## 报告问题

如果你发现 Bug 或有功能建议，请在 GitHub 上创建 Issue，并包含：
- 清晰的标题和描述
- 复现步骤（Bug 报告）
- 期望行为 vs 实际行为

## 许可证

参与贡献即表示你同意你的贡献将采用 MIT 许可证。
