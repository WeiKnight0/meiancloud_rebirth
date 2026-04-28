# Meian Cloud Rebirth Project Guide
[**简体中文**](README.zh-cn.md) | [English](#)

Developer-facing documentation for the Meian Cloud Rebirth repository. The website itself still uses the historical project name "Meian Cloud". This repository is a reset and continuation of the original [`r1Way/meiancloud`](https://github.com/r1Way/meiancloud) project. The current repository is [`WeiKnight0/meiancloud_rebirth`](https://github.com/WeiKnight0/meiancloud_rebirth). For a website-oriented introduction, see [intro/README.md](intro/README.md).

## Overview
Meian Cloud is a Django-based website project built to present the history, culture, and educational significance of Meian at Southeast University in digital form. This repository contains the reset codebase, deployment configuration, and supporting assets maintained for continued development.

![Project Preview](figs/home-page.png)

## Repository
- Original project: [https://github.com/r1Way/meiancloud](https://github.com/r1Way/meiancloud)
- Current reset version: [https://github.com/WeiKnight0/meiancloud_rebirth](https://github.com/WeiKnight0/meiancloud_rebirth)
- Intro docs: [intro/README.md](intro/README.md)

## Project Lineage
- Website name: `Meian Cloud`
- Current code repository name: `meiancloud_rebirth`
- Relationship: this repository is the reset and continued development branch of the original project

## Tech Stack
- Backend: Django 4.2, Python 3.11
- Frontend: Django Templates, HTML5, CSS3, JavaScript
- Database: SQLite by default, MySQL supported
- Deployment: Docker Compose, Gunicorn, Nginx
- Media handling: Pillow
- AI integration: Tencent Cloud SSE-based chat interface

## Architecture
The project uses a classic Django monolith structure with separate apps for page content, accounts, community interaction, and AI services.

Request flow in deployment mode:

```text
Browser
  -> Nginx
  -> Django (Gunicorn or runserver)
  -> SQLite or MySQL
```

## Project Components
- `meiancloud/core`: public content pages such as the homepage, Meian exhibition guide, FAQ, and about page
- `meiancloud/accounts`: registration, login, profile editing, password changes, and account deletion
- `meiancloud/community`: discussion area, replies, comment review, and moderation
- `meiancloud/ai`: chat API endpoint and Tencent Cloud AI integration
- `meiancloud/mysite`: Django project settings, root URLs, and WSGI/ASGI entrypoints
- `figs/`: README images and preview assets
- `intro/`: website-oriented bilingual introduction documents

## Directory Layout
```text
.
├── figs/
├── intro/
├── README.md
├── README.zh-cn.md
└── meiancloud/
    ├── accounts/
    ├── ai/
    ├── community/
    ├── core/
    ├── mysite/
    ├── Dockerfile
    ├── docker-compose.yml
    ├── docker-compose.override.yml
    ├── nginx.conf
    ├── requirements.txt
    └── manage.py
```

## Core Modules
### `core`
- Routes public pages such as `/`, `/findmeian/`, `/about/`, and `/question/`
- Renders template-based content pages
- Provides shared request context for templates

### `accounts`
- Uses Django's built-in auth system
- Extends user information through `UserProfile`
- Supports avatar upload, profile editing, password changes, and account deletion
- Includes `ensure_admin_user`, which creates or updates a default admin account from environment variables

### `community`
- Stores top-level comments and replies in a single `Comment` model
- Exposes a public discussion page and a superuser moderation page
- Supports approval-based visibility for comments

### `ai`
- Exposes `POST /api/chat/`
- Forwards user messages to Tencent Cloud's streaming chat service
- Returns the final generated reply as JSON

## Local Development
Prerequisites:
- Python 3.11
- `pip`

Setup:

```shell
git clone https://github.com/WeiKnight0/meiancloud_rebirth
cd meiancloud/meiancloud
cp .env.example .env
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py ensure_admin_user
python3 manage.py runserver
```

Default local access:
- Website: `http://127.0.0.1:8000`
- Admin: `http://127.0.0.1:8000/admin/`

## Environment Variables
Runtime configuration is stored in `meiancloud/.env`.

Important variables:
- `DJANGO_SECRET_KEY`: Django secret key
- `DJANGO_DEBUG`: whether debug mode is enabled
- `DJANGO_ALLOWED_HOSTS`: comma-separated allowed hosts
- `DB_ENGINE`: database backend
- `DB_NAME`: database name or SQLite file name
- `DB_USER`: database username
- `DB_PASSWORD`: database password
- `DB_HOST`: database host
- `DB_PORT`: database port
- `ADMIN_USERNAME`: default admin username
- `ADMIN_PASSWORD`: default admin password
- `ADMIN_EMAIL`: default admin email
- `MYSQL_ROOT_PASSWORD`: MySQL root password for Docker
- `MYSQL_DATABASE`: MySQL database name for Docker
- `MYSQL_USER`: MySQL user for Docker
- `MYSQL_PASSWORD`: MySQL password for Docker

Notes:
- `meiancloud/.env.example` defaults to SQLite so local setup works immediately
- `meiancloud/.env` should not contain real secrets in version control
- the startup commands used in Docker also run migrations, collect static files, and ensure the admin account exists

Default admin account in `.env.example`:
- Username: `admin`
- Password: `123456`

## Docker Deployment
Docker-related files are in `meiancloud/`:
- `docker-compose.yml`: base configuration, closer to production
- `docker-compose.override.yml`: development overrides
- `Dockerfile`: Django image build
- `nginx.conf`: reverse proxy and static/media serving

Development mode:

```shell
cd meiancloud
cp .env.example .env
docker compose up --build
```

This starts:
- `mysql`
- `django` with `runserver`
- `nginx`

Default development access points:
- Website: `http://localhost`
- Django directly: `http://localhost:8000`
- MySQL: `127.0.0.1:3307`
- Admin: `http://localhost/admin/`

Production-style startup:

```shell
cd meiancloud
docker compose -f docker-compose.yml up --build -d
```

In this mode, Django runs with Gunicorn and only Nginx is exposed externally.

## Switching to MySQL
The default `.env.example` uses SQLite:

```env
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
```

To switch Django to MySQL, update `meiancloud/.env`:

```env
DB_ENGINE=django.db.backends.mysql
DB_NAME=meianclouddata
DB_USER=meianclouddata
DB_PASSWORD=SRZyhMDrMrCaWdpA
DB_HOST=mysql
DB_PORT=3306
```

If you use the bundled MySQL container, keep these aligned as well:

```env
MYSQL_ROOT_PASSWORD=123456
MYSQL_DATABASE=meianclouddata
MYSQL_USER=meianclouddata
MYSQL_PASSWORD=SRZyhMDrMrCaWdpA
```

After switching the database backend, recreate containers and rerun migrations.

## Development Notes
- Templates and static assets are organized by app
- `STATIC_ROOT` is `meiancloud/staticfiles`
- `MEDIA_ROOT` is `meiancloud/media`
- `mysite/urls.py` mounts all application routes at the root level
- superuser-only moderation is implemented in `community/comment-management/`
- the AI service currently depends on a configured Tencent Cloud bot key in code

## Contributors
Thanks to all members of the Meian Cloud practice team.

Core contributors:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/r1Way">
        <img src="https://avatars.githubusercontent.com/r1Way" width="100px;" alt="r1Way avatar"/>
        <br />
        <sub><b>r1Way (Team Leader)</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/WeiKnight0">
        <img src="https://avatars.githubusercontent.com/weiknight0" width="100px;" alt="WeiKnight avatar"/>
        <br />
        <sub><b>WeiKnight (Core Developer)</b></sub>
      </a>
    </td>
  </tr>
</table>

## Copyright
- Historical materials related to Meian belong to Southeast University
- The website project is maintained by the Meian Cloud practice team
- The code license is MIT
- Image sources should be credited when required

## References
- Django docs: [https://docs.djangoproject.com/](https://docs.djangoproject.com/)
- MDN Web Docs: [https://developer.mozilla.org/](https://developer.mozilla.org/)
- Original repository: [https://github.com/r1Way/meiancloud](https://github.com/r1Way/meiancloud)
- Current repository: [https://github.com/WeiKnight0/meiancloud_rebirth](https://github.com/WeiKnight0/meiancloud_rebirth)
