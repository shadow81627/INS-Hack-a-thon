from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /degrees/
    url(r'^$', views.index, name='index'),
    # ex: /degrees/5/
    url(r'^(?P<course_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /degrees/year/2018
    url(r'^(?P<course_id>[0-9]+)/$', views.detail, name='detail'),
]
