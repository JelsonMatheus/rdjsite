from django.contrib import admin
from django.urls import path, re_path
from django.urls.conf import include

import notifications.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^inbox/notifications/', include(notifications.urls, namespace='notifications')),

    path('', include('site_forum.urls')),
]
