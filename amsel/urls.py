from django.conf.urls import patterns, url, include
from django.contrib import admin
import routers
from core.api.views import (
    PatientViewSet,
    HealthFacilityViewSet,
    CaseInvestigatorViewSet,
)

admin.autodiscover()

router = routers.TemplateRouter(template_name='index.html')
router.register(r'patients', PatientViewSet, base_name='patient')
router.register(r'health-facilities', HealthFacilityViewSet, base_name='healthfacility')
router.register(r'case-investigators', CaseInvestigatorViewSet, base_name='caseinvestigator')

urlpatterns = patterns('',
                       url(r'^submit$', 'core.views.submit', name='submit'),
                       url(r'^smswebhook$', 'core.views.smswebhook', name='smswebhook'),
                       url(r'^admin/', include(admin.site.urls)),
                       # API Routes
                       url(r'^', include(router.urls)),
                       # API Auth Urls
                       url(r'^api-auth/', include('rest_framework.urls',
                                                  namespace='rest_framework')),
                       )
