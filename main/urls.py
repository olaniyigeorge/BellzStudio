


from django.urls import path
from .views import *


app_name = "main"

urlpatterns = [
    path('', index, name="index"),
    path("about-us/", about, name="about-us"),
    path("contact/", contact, name="contact"),
    path("contact/<str:destination>/", contactType, name="contact_type")
]