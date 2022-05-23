from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from contact.api import CreateFeedback
from timeline.api import api_router

urlpatterns = [
                  path('admin/', admin.site.urls),

                  # Wagtail URLs
                  path('cms/', include(wagtailadmin_urls)),
                  path('documents/', include(wagtaildocs_urls)),
                  path('timeline/', include(wagtail_urls)),

                  # REST
                  path('api/v2/', api_router.urls),
                  path('api/feedback', CreateFeedback.as_view())

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
