# 快速开始

[English](quickstart.md) | [简体中文](#)

5 分钟内完成梅庵云迹的本地环境搭建。

## 前置条件

- Python 3.11+
- pip
- Git

## 本地开发

```bash
git clone https://github.com/WeiKnight0/meiancloud_rebirth
cd meiancloud_rebirth/meiancloud
```

创建环境配置文件：

```bash
cp .env.example .env
```

编辑 `.env`，至少设置以下内容：

```env
DJANGO_SECRET_KEY=your-random-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
```

安装依赖：

```bash
pip3 install -r requirements.txt
```

执行数据库迁移并创建管理员账号：

```bash
python3 manage.py migrate
python3 manage.py ensure_admin_user
```

启动开发服务器：

```bash
python3 manage.py runserver
```

浏览器访问：
- 网站：http://127.0.0.1:8000
- 后台管理：http://127.0.0.1:8000/admin/

默认管理员账号（来自 `.env.example`）：
- 用户名：`admin`
- 密码：`123456`

> **重要**：部署到生产环境前，请务必修改管理员密码和 `DJANGO_SECRET_KEY`。

## Docker 方式

也可以使用 Docker Compose 一键启动：

```bash
cd meiancloud_rebirth/meiancloud
cp .env.example .env
docker compose up --build
```

该命令会启动：
- `django`（Gunicorn 运行，端口 8000）
- `mysql` 数据库
- `nginx` 反向代理（端口 80）

通过 http://localhost 访问
