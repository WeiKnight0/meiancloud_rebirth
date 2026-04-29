# Nginx 配置

[English](nginx-configuration.md) | [简体中文](#)

## 概述

Nginx 作为反向代理，直接处理静态文件和媒体文件请求，动态请求转发给 Django/Gunicorn。

## 配置文件

配置挂载自 `meiancloud/nginx.conf`：

```nginx
server {
    listen 80;
    server_name _;

    client_max_body_size 20m;

    location /static/ {
        alias /app/staticfiles/;
    }

    location /media/ {
        alias /app/media/;
    }

    location / {
        proxy_pass http://django:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## 工作原理

| 路径 | 处理方 | 原因 |
|---|---|---|
| `/static/*` | Nginx 直接返回 | 速度快，CSS/JS/图片无需经过 Python |
| `/media/*` | Nginx 直接返回 | 用户上传文件不经过 Django |
| `/*` | Django（Gunicorn） | 动态内容 |

## 关键配置

### `client_max_body_size 20m`

设置最大上传大小为 20MB。这是 HTTP 层面的限制，控制文件上传（如头像）的最大体积。Django 自身的校验可能更严格。

### 代理头

| 头部 | 值 | 用途 |
|---|---|---|
| `Host` | `$host` | 保留原始主机名 |
| `X-Real-IP` | `$remote_addr` | 客户端真实 IP |
| `X-Forwarded-For` | `$proxy_add_x_forwarded_for` | 代理链中的 IP 列表 |
| `X-Forwarded-Proto` | `$scheme` | 原始协议（http/https） |

这些头部确保 Django 在反向代理后能获取正确的客户端信息。

## 自定义配置

### 添加 HTTPS

生产环境启用 HTTPS：

```nginx
server {
    listen 443 ssl;
    server_name your-domain.com;

    ssl_certificate /etc/nginx/ssl/cert.pem;
    ssl_certificate_key /etc/nginx/ssl/key.pem;

    # ... 其余配置
}

server {
    listen 80;
    server_name your-domain.com;
    return 301 https://$host$request_uri;
}
```

### 添加限流

```nginx
limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;

location /api/ {
    limit_req zone=api burst=20 nodelay;
    proxy_pass http://django:8000;
    # ...
}
```
