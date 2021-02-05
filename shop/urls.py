from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += i18n_patterns(
    path('', include('main.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)