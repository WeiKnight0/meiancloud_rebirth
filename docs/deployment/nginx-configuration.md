# Nginx Configuration

[简体中文](nginx-configuration.zh-cn.md) | [English](#)

## Overview

Nginx serves as a reverse proxy, handling static/media files directly and forwarding dynamic requests to Django/Gunicorn.

## Configuration

The configuration is mounted from `meiancloud/nginx.conf`:

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

## How It Works

| Path | Handler | Why |
|---|---|---|
| `/static/*` | Nginx direct | Fast, no Python overhead for CSS/JS/images |
| `/media/*` | Nginx direct | User uploads served without hitting Django |
| `/*` | Django (Gunicorn) | Dynamic content |

## Key Settings

### `client_max_body_size 20m`

Sets the maximum upload size to 20MB. This controls how large a file upload (e.g., avatar) can be at the HTTP level. Django's own validation may impose stricter limits.

### Proxy Headers

| Header | Value | Purpose |
|---|---|---|
| `Host` | `$host` | Preserves the original hostname |
| `X-Real-IP` | `$remote_addr` | Client's real IP address |
| `X-Forwarded-For` | `$proxy_add_x_forwarded_for` | IP chain for proxied requests |
| `X-Forwarded-Proto` | `$scheme` | Original protocol (http/https) |

These headers ensure Django receives the correct client information behind the proxy.

## Customization

### Adding HTTPS

For production with HTTPS, add SSL configuration:

```nginx
server {
    listen 443 ssl;
    server_name your-domain.com;

    ssl_certificate /etc/nginx/ssl/cert.pem;
    ssl_certificate_key /etc/nginx/ssl/key.pem;

    # ... rest of config
}

server {
    listen 80;
    server_name your-domain.com;
    return 301 https://$host$request_uri;
}
```

### Adding Rate Limiting

```nginx
limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;

location /api/ {
    limit_req zone=api burst=20 nodelay;
    proxy_pass http://django:8000;
    # ...
}
```
