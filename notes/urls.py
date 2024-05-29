from django.urls import path
from .views import * 


app_name = "notes"

urlpatterns = [
    path("", index, name="index"),
    path("write/", NewNote, name="write-note"),
    path("new-idea/", NewIdea, name="new-idea"),
    path("search/", Search, name="search"),
    path("note/<str:slug>/", NoteView, name="note"),
    path("d/<str:date>/", NoteDate, name="notes-by-date"),
    path("idea-tags/<str:slug>/", IdeaNotes, name="notes-by-idea"),


    # ----------- NOTE REACH    -------------
    path("n/join-network/", networks, name="join-network"),
    
    path("network/<str:name>/", network, name="network"),
    
    
]