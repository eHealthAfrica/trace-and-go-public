from django.conf.urls import patterns, url, include

from django.contrib import admin
from django.views.generic import RedirectView

admin.autodiscover()

from rest_framework import routers

from core.api.views import (
    PatientViewSet,
    HealthFacilityViewSet,
    CaseInvestigatorViewSet,
)

router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'health-facilities', HealthFacilityViewSet)
router.register(r'case-investigators', CaseInvestigatorViewSet)

urlpatterns = patterns('',

                       url(r'^submit$', 'core.views.submit', name='submit'),

                       url(r'^smswebhook$', 'core.views.smswebhook', name='smswebhook'),

                       url(r'^admin/', include(admin.site.urls)),

                       # API Routes
                       url(r'^api/', include(router.urls)),

                       # API Auth Urls
                       url(r'^api-auth/', include('rest_framework.urls',
                                                  namespace='rest_framework')),

                       # For now we alwys redirect to the admin login
                       url(r'^.*$', RedirectView.as_view(url='admin/', permanent=False), name='index')
                       )
