from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^novo_usuario/$', views.add_user, name='add_user'),
]
