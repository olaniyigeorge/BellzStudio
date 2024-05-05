from django.urls import path
from .views import * 


app_name = "notes"

urlpatterns = [
    path("", index, name="index"),
    path("write/", NewNote, name="write-note"),
    # path("<uuid:noteID>/", Note, name="note"),
    path("<str:date>/", NoteDate, name="notes-by-date"),
    path("idea-tags/<uuid:id>/", IdeaNotes, name="notes-by-idea"),
]