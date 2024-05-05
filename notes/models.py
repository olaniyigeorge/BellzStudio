from django.db import models
import uuid
# Create your models here.


class IdeaTag(models.Model):
    #slug = models.SlugField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)

    description = models.TextField(null=True, blank=True)


    def save(self, *args, **kwargs):
        self.name = f"#{self.name}"

        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
    

    def my_notes(self):
        return self.on_notes.all()



class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=120)
    text = models.TextField(null=False, blank=False)
    tags = models.ManyToManyField(IdeaTag, related_name='on_notes')



    written_at = models.DateTimeField(auto_now_add=True)



