# Quick Start

[简体中文](quickstart.zh-cn.md) | [English](#)

Get Meian Cloud running locally in under 5 minutes.

## Prerequisites

- Python 3.11+
- pip
- Git

## Setup

```bash
git clone https://github.com/WeiKnight0/meiancloud_rebirth
cd meiancloud_rebirth/meiancloud
```

Create an environment file:

```bash
cp .env.example .env
```

Edit `.env` and set at minimum:

```env
DJANGO_SECRET_KEY=your-random-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
```

Install dependencies:

```bash
pip3 install -r requirements.txt
```

Run migrations and create admin account:

```bash
python3 manage.py migrate
python3 manage.py ensure_admin_user
```

Start the development server:

```bash
python3 manage.py runserver
```

Open in browser:
- Website: http://127.0.0.1:8000
- Admin panel: http://127.0.0.1:8000/admin/

Default admin credentials (from `.env.example`):
- Username: `admin`
- Password: `123456`

> **Important**: Change the admin password and `DJANGO_SECRET_KEY` before deploying to production.

## Docker Setup

Alternatively, use Docker Compose:

```bash
cd meiancloud_rebirth/meiancloud
cp .env.example .env
docker compose up --build
```

This starts:
- `django` with Gunicorn on port 8000
- `mysql` database
- `nginx` reverse proxy on port 80

Access via http://localhost
