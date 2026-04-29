# Glossary

[简体中文](glossary.zh-cn.md) | [English](#)

| Term | Definition |
|---|---|
| **Meian** (梅庵) | A historical building at Southeast University, originally built in 1915 to commemorate Li Ruiqing. Now a cultural heritage site and the namesake of this project. |
| **Meian Cloud** (梅庵云迹) | The website project name. A digital platform for presenting Meian's history, culture, and educational significance. |
| **Red Culture** (红色文化) | Revolutionary culture and history associated with the Chinese Communist movement. Meian was a site for early Marxist education and Communist Youth League activities. |
| **Southeast University** (东南大学) | A major university in Nanjing, China. Meian is located on its Sipailou campus. |
| **Li Ruiqing** (李瑞清) | Also known by his courtesy name "Meian" (梅庵). First president of Liangjiang Normal School, educator, and calligrapher. The building is named after him. |
| **Tuan Er Da** (团二大) | The Second National Congress of the Communist Youth League of China, held at Meian in August 1923. A milestone in Chinese youth movement history. |
| **To Shanshan** (至善讲解团) | The volunteer explanation team at Southeast University that manages Meian visits and bookings. |
| **Swiper** | A JavaScript carousel library used on the homepage for image sliding. |
| **Gunicorn** | A Python WSGI HTTP server used in production to serve the Django application. |
| **CSRF** | Cross-Site Request Forgery. Django's CSRF protection requires tokens on state-changing requests. |
| **Session** | Django's server-side mechanism for maintaining user login state across requests. |
| **UserProfile** | The project's custom user profile model, extending Django's built-in `User` with avatar, nickname, gender, birthday, and signature fields. |
| **Comment** | The project's discussion model, supporting both top-level comments and threaded replies through a self-referencing foreign key. |
| **is_checked** | The moderation flag on `Comment`. When `False`, the comment is not publicly visible. Superusers approve comments by setting this to `True`. |
| **Prefetch** | A Django ORM optimization that fetches related objects in a single query, used to avoid N+1 query problems in the comment list. |
