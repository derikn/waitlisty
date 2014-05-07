from django.conf.urls import patterns, include, url
from registration.backends.default.views import RegistrationView
from waitlisty.forms import ProfileForm

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^waitlisty/', include('waitlisty.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'accounts/register/$', 
        RegistrationView.as_view(form_class = ProfileForm), 
        name = 'registration_register'),
	url(r'^accounts/', include('registration.backends.default.urls')),
	url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
	)