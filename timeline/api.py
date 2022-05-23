from rest_framework.response import Response
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet
from wagtail.images.api.v2.views import ImagesAPIViewSet

from timeline.models import Post

api_router = WagtailAPIRouter('wagtailapi')


class CustomPagesAPIViewSet(PagesAPIViewSet):
    def detail_view(self, request, pk):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response = Response(serializer.data)
        if isinstance(instance, Post):
            prev_sibling, next_sibling = instance.get_siblings_by_published_date()
            response.data["prev_sibling"] = {"slug": prev_sibling.slug,
                                             "title": prev_sibling.title} if prev_sibling else None
            response.data["next_sibling"] = {"slug": next_sibling.slug,
                                             "title": next_sibling.title} if next_sibling else None
        return response


api_router.register_endpoint('pages', CustomPagesAPIViewSet)
api_router.register_endpoint('images', ImagesAPIViewSet)
api_router.register_endpoint('documents', DocumentsAPIViewSet)
