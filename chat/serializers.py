from users.serializers import UserProfileSerializer
from .models import Conversation, DirectMessage, Message
from rest_framework import serializers


class DirectMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectMessage
        exclude = ('conversation_id',)


class ConversationListSerializer(serializers.ModelSerializer):
    initiator = UserProfileSerializer()
    receiver = UserProfileSerializer()
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['initiator', 'receiver', 'last_message']

    def get_last_message(self, instance):
        message = instance.message_set.first()
        if message:
            return DirectMessageSerializer(instance=message).data
        else:
            return None


class ConversationSerializer(serializers.ModelSerializer):
    initiator = UserProfileSerializer()
    receiver = UserProfileSerializer()
    message_set = DirectMessageSerializer(many=True)

    class Meta:
        model = Conversation
        fields = ['initiator', 'receiver', 'message_set']

class MessageSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    class Meta:
        model = Message
        fields = '__all__'