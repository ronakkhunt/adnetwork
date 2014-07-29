from django.conf.urls import patterns, include, url

from signup.views import p_signup, signup, login, p_login
from adnetwork.views import home
from django.views.generic.simple import direct_to_template




# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'adnetwork.views.home', name='home'),
    # url(r'^adnetwork/', include('adnetwork.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	url(r'^p_signup/$',p_signup),
	url(r'^signup/$',signup),
	url(r'^p_login/$',p_login),
	url(r'^login/$',login),
	url(r'^$',home),
	url(r'^home/$',home),
	(r'^advertiser/$', direct_to_template, {'template': 'advertiser.html','extra_context':{'title':"Advertiser"},}),
	(r'^publisher/$', direct_to_template, {'template': 'publisher.html','extra_context':{'title':"Publisher"},}),
	(r'^contactus/$', direct_to_template, {'template': 'contactus.html','extra_context':{'title':"Contact Us"},}),
	
	
	

	
)
