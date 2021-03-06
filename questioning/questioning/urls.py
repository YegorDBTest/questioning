from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include('questioning_app.urls')),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]
