from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from . import views

admin.autodiscover()

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}),
    path("register/", views.register_request),
    path("org_page/", views.org_page_request),
    path("tracker/", views.tracker),
    path("tracker/metric/", views.metrics_page_request),
    path("login/", views.login_request),
    path("logout/", views.logout_request),
    path("admin/", admin.site.urls),
    path("home/", views.home_page_request),
    path("", include("cms.urls")),
]

"""urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}),
    path("en/register/", views.register_request, name="register")
]

urlpatterns += i18n_patterns(path("admin/", admin.site.urls), path("", include("cms.urls")))"""

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
