from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('roofs/', include('roof_order.urls')),
    path('', include('roof_pages.urls')),
    path('user/', include('roof_user.urls')),
    path('__debug__/', include('debug_toolbar.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
