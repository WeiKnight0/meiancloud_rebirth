# Docker 部署

[English](docker-production.md) | [简体中文](#)

## 概述

梅庵云迹使用 Docker Compose，包含三个服务：

| 服务 | 镜像 | 端口 | 用途 |
|---|---|---|---|
| `mysql` | `mysql:8.0` | 3307（开发）/ 3306（内部） | 数据库 |
| `django` | 自定义（Dockerfile） | 8000（开发） | Django + Gunicorn |
| `nginx` | `nginx:alpine` | 80 | 反向代理 + 静态文件 |

## 开发模式

```bash
cd meiancloud
cp .env.example .env
docker compose up --build
```

开发模式使用 `docker-compose.override.yml`：
- Django 使用 `runserver`（支持代码热重载）
- 直接暴露 8000 端口访问 Django
- MySQL 暴露在 3307 端口供外部工具连接
- 源码目录挂载为 volume，支持实时编辑

访问地址：
- 网站：http://localhost
- Django 直连：http://localhost:8000
- MySQL：`127.0.0.1:3307`

## 生产模式

```bash
cd meiancloud
docker compose -f docker-compose.yml up --build -d
```

生产模式仅使用 `docker-compose.yml`：
- Django 使用 Gunicorn 运行（4 workers，2 threads）
- 仅通过 Nginx 暴露 80 端口
- MySQL 仅内部可达
- 使用命名卷存储静态文件、媒体文件和数据库

访问地址：
- 网站：http://your-server

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

要点：
- 基于 Python 3.11 slim 镜像
- 项目依赖外额外安装 Gunicorn
- 使用清华 PyPI 镜像加速国内构建

## 启动流程

每次容器启动时，Django 依次执行：

```bash
python manage.py migrate
python manage.py ensure_admin_user
python manage.py collectstatic --noinput
gunicorn mysite.wsgi:application --bind 0.0.0.0:8000 --workers 4 --threads 2
```

1. **migrate** — 执行数据库迁移
2. **ensure_admin_user** — 从环境变量创建/更新管理员账号
3. **collectstatic** — 收集静态文件到 `staticfiles/`
4. **gunicorn** — 启动 WSGI 服务器

## 命名卷

| 卷名 | 挂载点 | 用途 |
|---|---|---|
| `mysql_data` | `/var/lib/mysql` | MySQL 数据持久化 |
| `static_data` | `/app/staticfiles` | 收集的静态文件 |
| `media_data` | `/app/media` | 用户上传（头像） |

## 常用命令

```bash
# 查看日志
docker compose logs -f django

# 重启单个服务
docker compose restart django

# 进入 Django 容器
docker compose exec django bash

# 执行管理命令
docker compose exec django python manage.py shell

# 停止所有服务
docker compose down

# 停止并删除卷（完全重置）
docker compose down -v
```

## 环境变量

所有配置通过环境变量管理。完整列表和默认值见[环境变量参考](../guides/environment-variables.zh-cn.md)。

生产环境至少需要在 `.env` 或部署平台中设置密钥、允许访问的主机名、数据库连接和管理员密码。不要在生产环境复用开发示例密码。
