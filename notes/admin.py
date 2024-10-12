from django.contrib import admin
from .models import Note, IdeaTag, NotePrivacy, Reader
# Register your models here.


@admin.register(IdeaTag)
class IdeaTagAdmin(admin.ModelAdmin):
    list_display = ["slug", "name", "description" ]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ["slug", "title", "written_at", 'privacy_level']
    list_filter = ["tags", "written_at", "privacy_level"]
    search_fields = ["title", "text", ]


@admin.register(NotePrivacy)
class NotePrivacyAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "level"]
    list_filter = ["level"]
    search_fields = [ ]



@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "subscription_level"]
    list_filter = ["subscription_level"]
    search_fields = [ ]
