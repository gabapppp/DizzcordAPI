from django.db import models
import uuid

from django.contrib.auth.models import User


class ServerCategory(models.Model):
    title = models.CharField(max_length=25)
    icon = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title


class Channel(models.Model):
    title = models.CharField(max_length=100)
    topic = models.CharField(max_length=150)
    is_voice = models.BooleanField(default=False) # "False" is Text Channel.
   
    def __str__(self) -> str:
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=144)
    channels = models.ManyToManyField(Channel)

    def __str__(self) -> str:
        return self.title


class Server(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #picture = models.ImageField(
    #    upload_to=user_directory_path_picture, null=False)
    #banner = models.ImageField(
    #    upload_to=user_directory_path_banner, null=False)
    title = models.CharField(max_length=144)
    description = models.CharField(max_length=255, blank=True, default="")
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='server_owner')
    members = models.ManyToManyField(User, related_name='server_members')
    moderators = models.ManyToManyField(User, related_name='server_moderators')
    categories = models.ManyToManyField(Category)
    server_category = models.ForeignKey(ServerCategory, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.title