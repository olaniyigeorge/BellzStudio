from django.db import models
import uuid
from django.utils.text import slugify 
# Create your models here.


class IdeaTag(models.Model):
    slug = models.SlugField(max_length=160, primary_key=True, unique=True, blank=True)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.name[0] != "#":
            self.name = f"#{self.name}"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

    def my_notes(self):
        return self.on_notes.all()

class NotePrivacy(models.Model):
    name = models.CharField(max_length=150, unique=True)
    level = models.IntegerField(unique=True)

    class Meta:
        ordering = ('level',)

    def __str__(self):
        return f"{self.level}: {self.name}"

class Note(models.Model):
    slug = models.SlugField(max_length=160, primary_key=True, unique=True, blank=True)
    title = models.CharField(max_length=150)
    text = models.TextField(null=False, blank=False)
    tags = models.ManyToManyField(IdeaTag, related_name='on_notes')
    privacy_level = models.ForeignKey(NotePrivacy, on_delete=models.SET_NULL, null=True)
    written_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ('-written_at', ) 

    def __str__(self): 
        return self.title 
    




