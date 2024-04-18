from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(Voter)
class VoterAdmin(admin.ModelAdmin):
    list_display = ["id", "person"]


@admin.register(Election)
class ElectionAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "date", "registered_voters_no" ]


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = ["id", "acronym", "name"]