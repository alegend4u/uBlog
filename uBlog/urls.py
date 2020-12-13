from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from portfolio import views as p_views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  url(r'^$', p_views.about),
                  url(r'^portfolio', p_views.portfolio),
                  url(r'^contact', p_views.contact),
                  url(r'^favicon\.ico', RedirectView.as_view(url='/static/images/favicon.ico')),

                  # Wagtail URLs
                  path('cms/', include(wagtailadmin_urls)),
                  path('documents/', include(wagtaildocs_urls)),
                  path('timeline/', include(wagtail_urls)),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
