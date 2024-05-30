from django.db import models
import uuid
from django.utils.text import slugify

from main.models import User 
# Create your models here.


class IdeaTag(models.Model):
    slug = models.SlugField(max_length=40, primary_key=True, unique=True, blank=True)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, unique=True)
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


    # ---- Network Info ----
    # color_code = models.CharField(max_length=20, null=True)


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
    
def get_default_subscription_model():
    return NotePrivacy.objects.get(name="Guests")

class Reader(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False, related_name='reader_profile')

    subscription_level = models.ForeignKey(NotePrivacy, on_delete=models.SET(get_default_subscription_model), default=get_default_subscription_model )
    
    written_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    
    default =  {
        'id': "test-uuid",
        'user': {
                "id": "test-user-id-1",
                "email": "test-user-1"
        },
        'subscription_level': "test-uuid",
        'written-at': "test-uuid",
        'updated_at': "test-uuid",
        
    }

    class Meta: 
        ordering = ('-updated_at', ) 

    def __str__(self): 
        if self.user:
            return f"{self.user.email}" 
        else:
            return f"{self.default['user']['email']}" 




