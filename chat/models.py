from django.db import models
from django.contrib.auth.models import User
from servers.models import Channel


# Create your models here.
class Conversation(models.Model):
    initiator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="convo_starter"
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="convo_participant"
    )
    start_time = models.DateTimeField(auto_now_add=True)


class DirectMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='message_sender')
    text = models.CharField(max_length=1000)
    attachment = models.FileField(blank=True)
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.text}'

    class Meta:
        ordering = ('-timestamp',)


class Message(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='server_message_user', default="")
    body = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    #file = models.FileField(
    #    upload_to=user_directory_path, blank=True, null=True)
    channel = models.ForeignKey(
        Channel, on_delete=models.CASCADE, related_name='msg_channel', default='TEXT CHANNEL')
    is_read = models.BooleanField(default=False)

    # Handle for only Text Channel ...
    # def create(self):
    #     pass


    def __str__(self) -> str:
        return f'{self.body}'