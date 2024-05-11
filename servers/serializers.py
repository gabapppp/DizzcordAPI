from users.serializers import UserProfileSerializer
from django.db.models import fields
from rest_framework import serializers

from .models import Category, Server, ServerCategory, Channel


class ServerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerCategory
        fields = '__all__'


class ServerChannelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'


class ServerChannelCategoriesSerializer(serializers.ModelSerializer):
    text_channels = ServerChannelsSerializer(many=True, required=False)

    class Meta:
        model = Category
        fields = '__all__'


class ServerSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    members = UserProfileSerializer(many=True, required=False)
    moderators = UserProfileSerializer(many=True, required=False)
    categories = ServerChannelCategoriesSerializer(many=True, required=False)
    server_category = ServerCategorySerializer(required=False)

    class Meta:
        model = Server
        fields = '__all__'


class ServerDetailSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    members = UserProfileSerializer(many=True)
    moderators = UserProfileSerializer(many=True)

    class Meta:
        model = Server
        fields = '__all__'
        depth = 2