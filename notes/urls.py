from django.urls import path

from .api_v1_views import ApiV1Home



app_name = "notes"

urlpatterns = [
    # path("", index, name="index"),
    # path("write/", NewNote, name="write-note"),
    # # path("<uuid:noteID>/", Note, name="note"),
    # path("<str:date>/", NoteDate, name="notes-by-date"),
    # path("idea-tags/<uuid:id>/", IdeaNotes, name="notes-by-idea"),
    # path("new-idea/", NewIdea, name="new-idea"),
    # path("search/", Search, name="search"),
    # path("note/<str:slug>/", NoteView, name="note"),
    # path("d/<str:date>/", NoteDate, name="notes-by-date"),
    # path("idea-tags/<str:slug>/", IdeaNotes, name="notes-by-idea"),


    # # ----------- NOTE REACH    -------------
    # path("n/join-network/", networks, name="join-network"),
    # path("n/subscribe/", subscribe, name="subscribe"),
    # path("network/<int:level>/", network, name="network"),
    
    # ------ v1.API  ------
    path("v1", ApiV1Home.as_view(), name="api_home"),

]