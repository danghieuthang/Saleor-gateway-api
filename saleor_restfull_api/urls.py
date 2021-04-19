
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url

# version = getattr(settings, "API_VERSION")
# if version is None:
#     raise("API_VERSION must be config in settings")
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('api.urls', namespace="Product"))
]
