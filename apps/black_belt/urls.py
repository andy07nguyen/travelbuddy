from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^userlogin$', views.loginProcess),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
    url(r'^add$', views.add),
    url(r'^addprocess$', views.addprocess),
    url(r'^remove/(?P<id>\d+)/$', views.remove, name="remove_url"),
    url(r'^delete/(?P<id>\d+)/$', views.delete, name="delete_url"),
    url(r'^join/(?P<id>\d+)/$', views.join, name="join_url"),
    url(r'^show/(?P<id>\d+)/$', views.show, name="show_url"),
    url(r'^.+$', views.index) #PUT THIS LINE AT THE END!!!
]
