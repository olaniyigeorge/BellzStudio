from django.urls import path
from .api_v1_views import *

urlpatterns = [
    # ------ v1.API  ------
    path("v1", ApiV1Home.as_view(), name="api_home"),

]