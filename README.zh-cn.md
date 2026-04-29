# 梅庵云迹重置版项目说明
[**English**](README.md) | [简体中文](#)

这是一份面向开发者的项目文档。网站本身仍沿用“梅庵云迹 / Meian Cloud”这一项目名称，而当前代码仓库是原始项目 [`r1Way/meiancloud`](https://github.com/r1Way/meiancloud) 的重置版与延续版本，现仓库地址为 [`WeiKnight0/meiancloud_rebirth`](https://github.com/WeiKnight0/meiancloud_rebirth)。若你想先了解网站本身的用途、功能与意义，请查看 [intro/INTRODUCTION.zh-cn.md](intro/INTRODUCTION.zh-cn.md)。

## 项目概览
梅庵云迹是一个基于 Django 构建的网站项目，目标是以数字化方式展示东南大学梅庵相关的历史、文化与教育意义。当前仓库包含重置后的项目代码、部署配置以及继续开发所需的相关资源。

![项目预览](figs/home-page.png)

## 仓库说明
- 原始项目仓库：[https://github.com/r1Way/meiancloud](https://github.com/r1Way/meiancloud)
- 当前重置版仓库：[https://github.com/WeiKnight0/meiancloud_rebirth](https://github.com/WeiKnight0/meiancloud_rebirth)
- 网站介绍文档：[intro/INTRODUCTION.zh-cn.md](intro/INTRODUCTION.zh-cn.md)
- 技术文档：[docs/](docs/index.zh-cn.md)

## 项目沿革
- 网站名称：`梅庵云迹` / `Meian Cloud`
- 当前代码仓库名：`meiancloud_rebirth`
- 二者关系：当前仓库是原项目的重置版，并在此基础上继续开发

## 技术栈
- 后端：Django 4.2、Python 3.11
- 前端：Django Templates、HTML5、CSS3、JavaScript
- 数据库：默认 SQLite，支持 MySQL
- 部署：Docker Compose、Gunicorn、Nginx
- 媒体处理：Pillow

## 系统架构
项目采用典型的 Django 单体应用结构，通过不同 app 划分页面内容、用户系统和社区互动。

部署模式下的请求链路如下：

```text
浏览器
  -> Nginx
  -> Django (Gunicorn 或 runserver)
  -> SQLite 或 MySQL
```

## 项目组成
- `meiancloud/core`：公共内容页面，如首页、循迹梅庵、常见问题、关于我们等
- `meiancloud/accounts`：注册、登录、个人资料编辑、修改密码、注销账号
- `meiancloud/community`：评论区、回复、评论审核与管理
- `meiancloud/mysite`：Django 项目配置、根路由、WSGI/ASGI 入口
- `figs/`：README 预览图片等资源
- `intro/`：面向网站介绍的中英文文档

## 目录结构
```text
.
├── figs/
├── intro/
├── README.md
├── README.zh-cn.md
└── meiancloud/
    ├── accounts/
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

## 核心模块说明
### `core`
- 提供 `/`、`/findmeian/`、`/about/`、`/question/` 等公共页面路由
- 负责基于模板渲染网站主要内容页
- 提供模板共享上下文

### `accounts`
- 基于 Django 内置认证系统实现用户登录注册
- 通过 `UserProfile` 扩展用户资料
- 支持头像上传、资料修改、密码修改、账号注销
- 包含 `ensure_admin_user` 管理命令，可依据环境变量自动创建或更新管理员账号

### `community`
- 使用单一 `Comment` 模型存储主评论与回复
- 提供公开评论区与超级管理员审核页面
- 通过审核状态控制评论是否对外可见

## 本地开发
前置条件：
- Python 3.11
- `pip`

启动步骤：

```shell
git clone https://github.com/WeiKnight0/meiancloud_rebirth
cd meiancloud/meiancloud
cp .env.example .env
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py ensure_admin_user
python3 manage.py runserver
```

本地默认访问地址：
- 网站：`http://127.0.0.1:8000`
- 后台：`http://127.0.0.1:8000/admin/`

## 环境变量
项目运行配置集中放在 `meiancloud/.env` 中。

主要变量：
- `DJANGO_SECRET_KEY`：Django 密钥
- `DJANGO_DEBUG`：是否开启调试模式
- `DJANGO_ALLOWED_HOSTS`：允许访问的主机列表，使用逗号分隔
- `DB_ENGINE`：数据库后端
- `DB_NAME`：数据库名或 SQLite 文件名
- `DB_USER`：数据库用户名
- `DB_PASSWORD`：数据库密码
- `DB_HOST`：数据库主机
- `DB_PORT`：数据库端口
- `ADMIN_USERNAME`：默认管理员用户名
- `ADMIN_PASSWORD`：默认管理员密码
- `ADMIN_EMAIL`：默认管理员邮箱
- `MYSQL_ROOT_PASSWORD`：Docker 中 MySQL root 密码
- `MYSQL_DATABASE`：Docker 中 MySQL 数据库名
- `MYSQL_USER`：Docker 中 MySQL 用户名
- `MYSQL_PASSWORD`：Docker 中 MySQL 用户密码

说明：
- `meiancloud/.env.example` 默认使用 SQLite，便于本地直接启动
- `meiancloud/.env` 不应提交真实密钥或生产密码
- Docker 启动命令中会自动执行迁移、收集静态文件，并确保管理员账号存在

`.env.example` 默认管理员账号：
- 用户名：`admin`
- 密码：`123456`

## Docker 部署
Docker 相关文件位于 `meiancloud/`：
- `docker-compose.yml`：基础配置，偏生产风格
- `docker-compose.override.yml`：开发环境覆盖配置
- `Dockerfile`：Django 镜像构建文件
- `nginx.conf`：反向代理与静态资源配置

开发环境启动：

```shell
cd meiancloud
cp .env.example .env
docker compose up --build
```

该命令会启动：
- `mysql`
- 使用 `runserver` 的 `django`
- `nginx`

开发环境默认访问点：
- 网站：`http://localhost`
- Django 直连：`http://localhost:8000`
- MySQL：`127.0.0.1:3307`
- 后台：`http://localhost/admin/`

偏生产方式启动：

```shell
cd meiancloud
docker compose -f docker-compose.yml up --build -d
```

该模式下 Django 通过 Gunicorn 运行，对外仅暴露 Nginx。

## 切换到 MySQL
默认 `.env.example` 使用的是 SQLite：

```env
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
```

如果要切换为 MySQL，请修改 `meiancloud/.env`：

```env
DB_ENGINE=django.db.backends.mysql
DB_NAME=meianclouddata
DB_USER=meianclouddata
DB_PASSWORD=SRZyhMDrMrCaWdpA
DB_HOST=mysql
DB_PORT=3306
```

如果使用项目自带 MySQL 容器，也请保持这些值一致：

```env
MYSQL_ROOT_PASSWORD=123456
MYSQL_DATABASE=meianclouddata
MYSQL_USER=meianclouddata
MYSQL_PASSWORD=SRZyhMDrMrCaWdpA
```

切换数据库后，建议重新创建容器并重新执行迁移。

## 开发说明
- 模板与静态资源按 app 分目录组织
- `STATIC_ROOT` 为 `meiancloud/staticfiles`
- `MEDIA_ROOT` 为 `meiancloud/media`
- `mysite/urls.py` 将各 app 路由统一挂载到根路径下
- 评论审核页仅允许超级管理员访问

## 开发团队
感谢梅庵云迹实践团全体成员的努力与投入。

核心开发者：

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/r1Way">
        <img src="https://avatars.githubusercontent.com/r1Way" width="100px;" alt="r1Way 头像"/>
        <br />
        <sub><b>r1Way（组长）</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/WeiKnight0">
        <img src="https://avatars.githubusercontent.com/weiknight0" width="100px;" alt="WeiKnight 头像"/>
        <br />
        <sub><b>WeiKnight（核心开发者）</b></sub>
      </a>
    </td>
  </tr>
</table>

## 版权声明
- 梅庵历史资料版权归东南大学所有
- 网站项目由梅庵云迹实践团维护
- 代码开源协议为 MIT
- 图片素材如有要求应注明来源

## 参考资料
- Django 文档：[https://docs.djangoproject.com/](https://docs.djangoproject.com/)
- MDN Web Docs：[https://developer.mozilla.org/zh-CN/](https://developer.mozilla.org/zh-CN/)
- 原始项目仓库：[https://github.com/r1Way/meiancloud](https://github.com/r1Way/meiancloud)
- 当前项目仓库：[https://github.com/WeiKnight0/meiancloud_rebirth](https://github.com/WeiKnight0/meiancloud_rebirth)
