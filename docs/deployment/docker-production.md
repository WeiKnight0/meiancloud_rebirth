# Docker Deployment

[简体中文](docker-production.zh-cn.md) | [English](#)

## Overview

Meian Cloud uses Docker Compose with three services:

| Service | Image | Port | Purpose |
|---|---|---|---|
| `mysql` | `mysql:8.0` | 3307 (dev) / 3306 (internal) | Database |
| `django` | Custom (Dockerfile) | 8000 (dev) | Django + Gunicorn |
| `nginx` | `nginx:alpine` | 80 | Reverse proxy + static files |

## Development Mode

```bash
cd meiancloud
cp .env.example .env
docker compose up --build
```

This uses `docker-compose.override.yml` which:
- Runs Django with `runserver` (auto-reload enabled)
- Exposes port 8000 directly for Django
- Exposes MySQL on port 3307 for external tools
- Mounts source code as a volume for live editing

Access:
- Website: http://localhost
- Django direct: http://localhost:8000
- MySQL: `127.0.0.1:3307`

## Production Mode

```bash
cd meiancloud
docker compose -f docker-compose.yml up --build -d
```

This uses only `docker-compose.yml` which:
- Runs Django with Gunicorn (4 workers, 2 threads)
- Only exposes Nginx on port 80
- MySQL is internal-only
- Uses named volumes for static files, media, and database

Access:
- Website: http://your-server

## Dockerfile

```dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple \
    PIP_DEFAULT_TIMEOUT=300

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY . .
```

Key points:
- Uses Python 3.11 slim image
- Installs Gunicorn alongside project dependencies
- Uses Tsinghua PyPI mirror for faster builds in China

## Startup Sequence

On each container start, Django runs:

```bash
python manage.py migrate
python manage.py ensure_admin_user
python manage.py collectstatic --noinput
gunicorn mysite.wsgi:application --bind 0.0.0.0:8000 --workers 4 --threads 2
```

1. **migrate** — Apply database migrations
2. **ensure_admin_user** — Create/update admin account from env vars
3. **collectstatic** — Gather static files into `staticfiles/`
4. **gunicorn** — Start the WSGI server

## Named Volumes

| Volume | Mount Point | Purpose |
|---|---|---|
| `mysql_data` | `/var/lib/mysql` | MySQL data persistence |
| `static_data` | `/app/staticfiles` | Collected static files |
| `media_data` | `/app/media` | User uploads (avatars) |

## Useful Commands

```bash
# View logs
docker compose logs -f django

# Restart a single service
docker compose restart django

# Enter Django container
docker compose exec django bash

# Run management commands
docker compose exec django python manage.py shell

# Stop all services
docker compose down

# Stop and remove volumes (full reset)
docker compose down -v
```

## Environment Variables

All configuration is through environment variables. See [Environment Variables Reference](../guides/environment-variables.md) for the complete list.

In production, set these in `.env` or your deployment platform:

```env
DJANGO_SECRET_KEY=<random-secret>
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=your-domain.com
DB_ENGINE=django.db.backends.mysql
DB_NAME=meianclouddata
DB_USER=meianclouddata
DB_PASSWORD=<secure-password>
DB_HOST=mysql
DB_PORT=3306
ADMIN_PASSWORD=<secure-admin-password>
```
