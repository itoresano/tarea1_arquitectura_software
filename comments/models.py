
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Comment(models.Model):
    comment_text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')
    ip_client = models.CharField(max_length=400)
    ip_server = models.CharField(max_length=400)

    def __str__(self):
        return self.comment_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
