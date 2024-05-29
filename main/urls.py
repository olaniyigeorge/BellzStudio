


from django.urls import path
from .views import *


app_name = "main"

urlpatterns = [
    path('', index, name="index"),
    path("about-us/", about, name="about-us"),
    path("contact/", contact, name="contact"),
    path("contact/<str:destination>/", contactType, name="contact_type"),


    # ----------- USER MANGEMENT   -------------
    path("profile/me", profile, name="profile"),


    # ----------- USER AUTHENTICATION   -------------
    path("get-familiar", signUp, name="sign-up"),
    path("sign-in", signIn, name="sign-in"),
    path("sign-out", signOut, name="sign-out"),


    
    
]