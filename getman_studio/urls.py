"""getman_studio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from django.contrib import admin
from getman_studio import views
from shop import urls
from django.conf.urls.static import static
import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.gallery, name='gallery'),
    url(r'^workshop/', views.workshop, name='workshop'),
    url(r'^contacts/', views.contacts, name='contacts'),
]

urlpatterns += urls.urlpatterns
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
