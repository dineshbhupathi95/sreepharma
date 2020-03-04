from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$', views.home,name='home'),
    url(r'users/$', views.usersinformation.as_view())
]