from django.db import models

class QueueItem(models.Model):
  text = models.CharField(max_length=200)
