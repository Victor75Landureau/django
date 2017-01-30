from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^home$', views.home),
    url(r'^$', views.accueil, name='accueil'),
    url(r'^article/(\d+)$', views.lire, name='lire'),
    url(r'^page$', views.page),
    url(r'^redirection$', views.view_redirection),
    url(r'^date$', views.date_actuelle),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition)
]

"""    url(r'^article/(?P<id_article>\d+)$', views.view_article, name="afficher_article"),
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})$', views.list_articles),"""