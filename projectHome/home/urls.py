from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^movie/(?P<movie_id>[0-9]+)/$', views.movie, name='movie'),
    url(r'^movie/(?P<movie_id>[0-9]+)/watch/$', views.watch, name='watch'),
]
