from django.db.models.signals import post_save, pre_save

from main.models import User
from .models import IdeaTag, Note, Reader
from django.utils.text import slugify 
import string, random 
from django.dispatch import receiver 

# ------ UTILS ------


  
def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits): 
    return ''.join(random.choice(chars) for _ in range(size)) 

def unique_slug_generator(instance, new_slug = None): 
    if new_slug is not None: 
        slug = new_slug 
    else: 
        slug = slugify(instance.title) 
    Klass = instance.__class__ 
    max_length = Klass._meta.get_field('slug').max_length 
    title_length = Klass._meta.get_field('title').max_length 
    diff_length = max_length - title_length 
    randstr_length = random.randint(1, 10)
    slug = slug[:max_length] 
    qs_exists = Klass.objects.filter(slug = slug).exists() 
      
    if qs_exists: 
        # new_slug = f"{slug}-{random_string_generator(size = 4)}"
        new_slug = "{slug}-{randstr}".format( 
            slug = slug[:max_length-5], 
            randstr = random_string_generator(size = randstr_length)) 
              
        return unique_slug_generator(instance, new_slug = new_slug) 
    return slug

def unique_tag_slug_generator(instance, new_slug = None): 
    if new_slug is not None: 
        slug = new_slug 
    else: 
        slug = slugify(instance.name) 
    Klass = instance.__class__ 
    max_length = Klass._meta.get_field('slug').max_length 
    title_length = Klass._meta.get_field('name').max_length 
    diff_length = max_length - title_length 
    randstr_length = random.randint(1, diff_length)
    slug = slug[:max_length] 
    qs_exists = Klass.objects.filter(slug = slug).exists() 
      
    if qs_exists: 
        # new_slug = f"{slug}-{random_string_generator(size = 4)}"
        new_slug = "{slug}-{randstr}".format( 
            slug = slug[:max_length-5], 
            randstr = random_string_generator(size = randstr_length)) 
              
        return unique_tag_slug_generator(instance, new_slug = new_slug) 
    return slug


# ------ SIGNALS ------

@receiver(pre_save, sender=Note) 
def pre_save_receiver(sender, instance, *args, **kwargs): 
   if not instance.slug: 
       instance.slug = unique_slug_generator(instance) 

@receiver(pre_save, sender=IdeaTag) 
def pre_save_receiver(sender, instance, *args, **kwargs): 
   if not instance.slug: 
       instance.slug = unique_tag_slug_generator(instance) 


@receiver(post_save, sender=User) 
def create_reader_profile(sender, instance, created, *args, **kwargs): 
   if created:
        try:
            Reader.objects.create(user=instance)
            print("Reader Profile created")
            return 
        except Exception as e:
            print(f"Reader profile wasn't created: {e}")
            return None
        