from django.db import models

class LineItem(models.Model):
  text = models.CharField(max_length=200)
