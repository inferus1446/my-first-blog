from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('news/', include('news.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
'''urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)'''