from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_notification", default="")
    message = models.CharField(max_length=100, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ["-timestamp"]