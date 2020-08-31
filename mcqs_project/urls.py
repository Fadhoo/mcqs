from django.conf.urls import url, include
from django.contrib import admin
from App import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^quiz/', include('App.urls')),
    url(r'^login', views.welcome, name="login"),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', views.welcome, name="home"),
]
