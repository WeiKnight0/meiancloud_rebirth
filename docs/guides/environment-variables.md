# Environment Variables Reference

[简体中文](environment-variables.zh-cn.md) | [English](#)

All configuration is managed through environment variables. In Docker Compose, these are injected via the `.env` file or compose environment settings.

Values shown as defaults are for local development only unless explicitly stated. Set unique secrets and passwords for production.

## Required Variables

These must be set or the application will fail to start.

| Variable | Type | Description |
|---|---|---|
| `DJANGO_SECRET_KEY` | string | Django secret key for cryptographic signing |

## Django Configuration

| Variable | Default | Description |
|---|---|---|
| `DJANGO_SECRET_KEY` | *(required)* | Secret key — generate a random value for production |
| `DJANGO_DEBUG` | `False` | Enable debug mode (`True`/`False`) |
| `DJANGO_ALLOWED_HOSTS` | *(empty)* | Comma-separated list of allowed hostnames |
| `CSRF_TRUSTED_ORIGINS` | *(empty)* | Comma-separated list of trusted origins for CSRF |

## Database

### SQLite (default)

| Variable | Default | Description |
|---|---|---|
| `DB_ENGINE` | `django.db.backends.sqlite3` | Database backend |
| `DB_NAME` | `db.sqlite3` | SQLite file path |

### MySQL

Set `DB_ENGINE` to `django.db.backends.mysql` and provide these:

| Variable | Required | Description |
|---|---|---|
| `DB_ENGINE` | Yes | Must be `django.db.backends.mysql` |
| `DB_NAME` | Yes | Database name |
| `DB_USER` | Yes | Database username |
| `DB_PASSWORD` | Yes | Database password |
| `DB_HOST` | No (default: `localhost`) | Database host |
| `DB_PORT` | No (default: `3306`) | Database port |

## Admin Account

Used by the `ensure_admin_user` management command.

| Variable | Default | Description |
|---|---|---|
| `ADMIN_USERNAME` | `admin` | Default admin username |
| `ADMIN_PASSWORD` | *(required)* | Default admin password |
| `ADMIN_EMAIL` | `admin@example.com` | Default admin email |

## Docker / MySQL Container

These variables configure the MySQL service in Docker Compose.

| Variable | Default | Description |
|---|---|---|
| `MYSQL_ROOT_PASSWORD` | `123456` | MySQL root password |
| `MYSQL_DATABASE` | `meianclouddata` | MySQL database name |
| `MYSQL_USER` | `meianclouddata` | MySQL application user |
| `MYSQL_PASSWORD` | `SRZyhMDrMrCaWdpA` | MySQL application password |

## Example `.env` File

```env
DJANGO_SECRET_KEY=my-random-secret-key-here
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3

ADMIN_USERNAME=admin
ADMIN_PASSWORD=changeme
ADMIN_EMAIL=admin@example.com

CSRF_TRUSTED_ORIGINS=http://127.0.0.1,http://localhost

MYSQL_ROOT_PASSWORD=changeme
MYSQL_DATABASE=meianclouddata
MYSQL_USER=meianclouddata
MYSQL_PASSWORD=changeme
```
