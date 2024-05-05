from django.contrib import admin
from .models import Note, IdeaTag
# Register your models here.


@admin.register(IdeaTag)
class IdeaTagAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description" ]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "written_at"]
    list_filter = ["tags", "written_at"]
    search_fields = ["title", "text", ]
