from .urls_accounts import urlpatterns as account_urlpatterns
from .urls_ai import urlpatterns as ai_urlpatterns
from .urls_community import urlpatterns as community_urlpatterns
from .urls_content import urlpatterns as content_urlpatterns

app_name = "home"

urlpatterns = [
    *content_urlpatterns,
    *account_urlpatterns,
    *community_urlpatterns,
    *ai_urlpatterns,
]
