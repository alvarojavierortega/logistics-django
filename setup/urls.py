from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('api/', include('logistics.urls')),
    path('api/dummy/', include('dummy.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT} )
] 

