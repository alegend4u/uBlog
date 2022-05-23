from rest_framework import generics, mixins

from contact.serializers import FeedbackSerializer


class CreateFeedback(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = FeedbackSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
