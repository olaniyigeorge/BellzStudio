from django.urls import path
from .consumers import TrackElectionComsumer



websocket_urlpatterns = [
    path("ws/dev-stories/dc/<id>/", TrackElectionComsumer.as_asgi()),

]