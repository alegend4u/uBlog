from rest_framework.serializers import ModelSerializer

from contact.models import Feedback


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
