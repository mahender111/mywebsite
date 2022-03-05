from rest_framework.serializers import ModelSerializer

from blog import models


class Postserializer(ModelSerializer):

    class Meta:
        model = models.Post
        fields = "__all__"