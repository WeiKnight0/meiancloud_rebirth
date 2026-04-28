from django.contrib import admin
from django.urls import include, path
from django.contrib import admin
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static

from core.errors import page_not_found, permission_denied, server_error

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('ai.urls', 'ai'), namespace='ai')),
    path('', include(('core.urls', 'core'), namespace='core')),
    path('', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('', include(('community.urls', 'community'), namespace='community')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found
handler500 = server_error
handler403 = permission_denied
