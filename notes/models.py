from django.db import models
import uuid
# Create your models here.


class IdeaTag(models.Model):
    name = models.CharField(max_length=150)


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=120)
    text = models.TextField(null=False, blank=False)
    tags = models.ManyToManyField(IdeaTag)

