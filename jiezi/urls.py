from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from jiezi import views


urlpatterns = [
    # celery progress app
    path('celery-progress/', include('celery_progress.urls')),
    # rest framework api
    path('api_auth/', include('rest_framework.urls',
                              namespace='rest_framework')),

    # app urls
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('learning/', include('learning.urls')),
    path('jiezi_admin/', include('jiezi_admin.urls')),

    # front-page urls
    path('index/', views.index, name="index"),
    path('', RedirectView.as_view(url='index')),
    path('about_us/', views.about_us, name="about_us"),
    path('api_root/', views.api_root),

    #front-end testing urls
    #path('',TemplateView.as_view(url = 'index.html'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
