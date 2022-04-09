"""givntek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from join import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', views.index, name='index'),
    path('join', views.join, name='join'),
    path('contribute', views.contribute, name='contribute'),
    path('documentation', views.docs, name='documentation'),
    path('get-help', views.getHelp, name='get-help'),
    path('docs/code/activitypub', views.activitypub, name='activitypub'),
    path('docs/code/permissions', views.permissions, name='permissions'),
    path('docs/help/developers', views.developers, name='developers'),
    path('docs/help/translations', views.translations, name='translations'),
    path('docs/help/customize', views.customize, name='customize'),
    path('docs/run/production', views.production, name='production'),
    path('docs/run/updating', views.updating, name='updating'),
    path('docs/run/images', views.images, name='images'),
    path('docs/run/docker', views.docker, name='docker'),
]
