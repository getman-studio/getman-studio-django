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
from .settings import MEDIA_URL
from .settings import MEDIA_ROOT

from .views import gallery, workshop, contacts
from . import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', gallery, name='gallery'),
    url(r'^workshop/', workshop, name='workshop'),
    url(r'^workshop/(?P<page>\d+)/$', views.workshop),
    url(r'^contacts/', contacts, name='contacts'),
]

urlpatterns += urls.urlpatterns
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
