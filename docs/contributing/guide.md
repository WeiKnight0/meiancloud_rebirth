# Contributing Guide

[简体中文](guide.zh-cn.md) | [English](#)

Thank you for your interest in contributing to Meian Cloud!

## Getting Started

### 1. Fork and Clone

```bash
# Fork on GitHub, then:
git clone https://github.com/<your-username>/meiancloud_rebirth.git
cd meiancloud_rebirth
```

### 2. Set Up Development Environment

```bash
cd meiancloud
cp .env.example .env
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py ensure_admin_user
python3 manage.py runserver
```

Or with Docker:

```bash
cd meiancloud
cp .env.example .env
docker compose up --build
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

## Branch Naming

| Prefix | Purpose | Example |
|---|---|---|
| `feature/` | New feature | `feature/comment-search` |
| `fix/` | Bug fix | `fix/avatar-upload-error` |
| `docs/` | Documentation | `docs/update-deployment-guide` |
| `refactor/` | Code refactoring | `refactor/separate-community-views` |

## Making Changes

### Before You Start

1. Check existing issues and PRs to avoid duplicates
2. For large changes, open an issue first to discuss the approach

### While Working

1. Keep commits focused — one logical change per commit
2. Write clear commit messages (see below)
3. Test your changes locally before pushing

### Commit Messages

Use imperative mood:

```
Add comment search feature

- Add search field to comment list page
- Add filter queryset in freetotalk_page view
- Add pagination for search results
```

Good: `Add avatar upload validation`
Bad: `Fixed stuff` or `Update views.py`

## Pull Request Process

1. Push your branch to your fork
2. Open a Pull Request against `main`
3. Fill in the PR description:
   - What the change does
   - Why it's needed
   - How to test it
4. Wait for CI checks and code review
5. Address review feedback if any

## Code Review Expectations

- All PRs require at least one review before merge
- CI checks must pass
- Reviewers may request changes — this is normal and expected

## Reporting Issues

When reporting a bug, include:
- Steps to reproduce
- Expected behavior
- Actual behavior
- Python/Django version
- Browser (if frontend issue)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
