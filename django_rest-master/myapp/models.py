# models.py

from django.conf import settings
from django.db import models
# from ruamel_yaml.timestamp import TimeStamp
#from utils.models import TimestampZone

#from datetime import datetime
#from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message      = models.TextField()
    is_public   = models.BooleanField(default=False, db_index=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

