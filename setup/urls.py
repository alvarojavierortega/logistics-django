from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/', include('logistics.urls')),
    path('api/dummy/', include('dummy.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
