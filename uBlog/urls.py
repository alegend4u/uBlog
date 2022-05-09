from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from uBlog.api import api_router

urlpatterns = [
                  path('admin/', admin.site.urls),
                  # url(r'^$', p_views.about),
                  # url(r'^portfolio', p_views.portfolio),
                  # url(r'^contact', p_views.contact),
                  # url(r'^favicon\.ico', RedirectView.as_view(url='/static/images/favicon.ico')),

                  # Wagtail URLs
                  path('cms/', include(wagtailadmin_urls)),
                  path('documents/', include(wagtaildocs_urls)),
                  path('timeline/', include(wagtail_urls)),

                  # REST
                  path('api/v2/', api_router.urls)

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
