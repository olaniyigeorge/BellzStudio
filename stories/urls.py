from django.urls import path
from .views import *

app_name = "stories"


urlpatterns = [
    path("", index, name="stories_index"),

    # ------ DemoCraty ------
    path("dc/", DemoCratyIndex, name="dc_Index"),
    path("dc/home", DemoCratyDemo, name="dc_home"),
    path("dc/<uuid:id>", ElectionDetails, name="election_details"),
    path("dc/<uuid:id>/register", ElectionRegistration, name="election_registration"),
    path("dc/<uuid:id>/vote", Vote, name="vote"),

]   