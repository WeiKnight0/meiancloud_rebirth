# 环境变量参考

[English](environment-variables.md) | [简体中文](#)

所有配置通过环境变量管理。Docker Compose 中通过 `.env` 文件或 compose 环境设置注入。

除非特别说明，默认值仅用于本地开发。生产环境必须设置独立的密钥和密码。

## 必填变量

以下变量必须设置，否则应用将无法启动。

| 变量 | 类型 | 说明 |
|---|---|---|
| `DJANGO_SECRET_KEY` | string | Django 密钥，用于加密签名 |

## Django 配置

| 变量 | 默认值 | 说明 |
|---|---|---|
| `DJANGO_SECRET_KEY` | *（必填）* | 密钥 — 生产环境请生成随机值 |
| `DJANGO_DEBUG` | `False` | 是否开启调试模式（`True`/`False`） |
| `DJANGO_ALLOWED_HOSTS` | *（空）* | 允许访问的主机名，逗号分隔 |
| `CSRF_TRUSTED_ORIGINS` | *（空）* | CSRF 可信来源，逗号分隔 |

## 数据库

### SQLite（默认）

| 变量 | 默认值 | 说明 |
|---|---|---|
| `DB_ENGINE` | `django.db.backends.sqlite3` | 数据库后端 |
| `DB_NAME` | `db.sqlite3` | SQLite 文件路径 |

### MySQL

将 `DB_ENGINE` 设为 `django.db.backends.mysql` 并提供以下变量：

| 变量 | 必填 | 说明 |
|---|---|---|
| `DB_ENGINE` | 是 | 必须为 `django.db.backends.mysql` |
| `DB_NAME` | 是 | 数据库名 |
| `DB_USER` | 是 | 数据库用户名 |
| `DB_PASSWORD` | 是 | 数据库密码 |
| `DB_HOST` | 否（默认：`localhost`） | 数据库主机 |
| `DB_PORT` | 否（默认：`3306`） | 数据库端口 |

## 管理员账号

供 `ensure_admin_user` 管理命令使用。

| 变量 | 默认值 | 说明 |
|---|---|---|
| `ADMIN_USERNAME` | `admin` | 默认管理员用户名 |
| `ADMIN_PASSWORD` | *（必填）* | 默认管理员密码 |
| `ADMIN_EMAIL` | `admin@example.com` | 默认管理员邮箱 |

## Docker / MySQL 容器

以下变量配置 Docker Compose 中的 MySQL 服务。

| 变量 | 默认值 | 说明 |
|---|---|---|
| `MYSQL_ROOT_PASSWORD` | `123456` | MySQL root 密码 |
| `MYSQL_DATABASE` | `meianclouddata` | MySQL 数据库名 |
| `MYSQL_USER` | `meianclouddata` | MySQL 应用用户 |
| `MYSQL_PASSWORD` | `SRZyhMDrMrCaWdpA` | MySQL 应用密码 |

## `.env` 文件示例

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
