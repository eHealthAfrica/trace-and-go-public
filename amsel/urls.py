from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

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
                       # `/submit` is unauthenticated and is possible not used, so let's not expose it
                       # url(r'^submit$', 'core.views.submit', name='submit'),

                       url(r'^smswebhook$', 'core.views.smswebhook', name='smswebhook'),
                       url(r'^admin/', include(admin.site.urls)),
                       # API Routes
                       url(r'^$', login_required(TemplateView.as_view(template_name="index.html"))),
                       url(r'^', include(router.urls), ),
                       url(r'^v1/', include(router.urls, namespace='v1')),
                       # API Auth Urls
                       url(r'^api-auth/', include('rest_framework.urls',
                                                  namespace='rest_framework')),
                       url(r'^accounts/login/$',
                           'django.contrib.auth.views.login', {'template_name': 'login.html'}),
                       url(r'^accounts/logout/$',
                           'django.contrib.auth.views.logout',
                           {'template_name': 'logout.html', 'next_page': '/accounts/login/'}
                           ),
                       )
