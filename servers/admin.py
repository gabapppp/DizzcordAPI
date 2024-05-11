from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Server)
admin.site.register(ServerCategory)
admin.site.register(Category)
admin.site.register(Channel)