from django.conf.urls import patterns, url

from waitlisty import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^disclaimer', views.disclaimer, name='disclaimer'),
	url(r'^login/$', views.login_user, name='login'),
	url(r'^addparent$', views.AddParent.as_view(), name='parent-new'),
	url(r'^addchild$', views.AddChild.as_view(), name='child-new'),
	)