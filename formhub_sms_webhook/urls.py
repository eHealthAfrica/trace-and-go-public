from django.conf.urls import patterns, url, include

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'core.views.home', name='home'),
    url(r'^submit$', 'core.views.submit', name='submit'),
    
    url(r'^query$', 'core.views.query', name='query'),

    
    url(r'^admin/', include(admin.site.urls)),

)
