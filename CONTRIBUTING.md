# Contributing Guide

[简体中文](CONTRIBUTING.zh-cn.md) | [English](#)

Thank you for your interest in contributing to Meian Cloud! This guide explains how to get started.

## How to Contribute

### 1. Fork the Repository

Click the "Fork" button on GitHub to create your own copy.

### 2. Clone Your Fork

```bash
git clone https://github.com/<your-username>/meiancloud_rebirth.git
cd meiancloud_rebirth
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

Branch naming convention:
- `feature/xxx` — New feature
- `fix/xxx` — Bug fix
- `docs/xxx` — Documentation only

### 4. Make Changes

Follow the code style conventions:
- Python: PEP 8
- Templates: follow existing indentation patterns
- Commit messages: use imperative mood ("Add feature" not "Added feature")

### 5. Test Locally

```bash
cd meiancloud
cp .env.example .env
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

### 6. Commit and Push

```bash
git add .
git commit -m "Add your descriptive commit message"
git push origin feature/your-feature-name
```

### 7. Open a Pull Request

Go to your fork on GitHub and click "New Pull Request". Describe:
- What the change does
- Why it's needed
- How to test it

## Code Style

### Python
- Follow [PEP 8](https://peps.python.org/pep-0008/)
- Use descriptive variable and function names
- Add docstrings to new functions and classes

### Templates
- Match existing indentation (4 spaces)
- Use Django template tags consistently

### Git
- Keep commits focused (one logical change per commit)
- Write clear commit messages

## Reporting Issues

If you find a bug or have a feature request, please open an issue on GitHub with:
- A clear title and description
- Steps to reproduce (for bugs)
- Expected vs actual behavior

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
