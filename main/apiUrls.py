from django.urls import path
from .api_v1_views import *
from rest_framework_simplejwt.views import (
    TokenVerifyView,
    TokenObtainPairView,
    TokenRefreshView,
)




urlpatterns = [
    # ------ v1.API  ------
   path("v1-users", UserView.as_view(), name="users"),
    path("v1-user/<uuid:id>", UserDetailView.as_view(), name="user_details"),

    # ---- Auth ----
    path('v1-token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('v1-token/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1-token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # ----- Profile -----
    path("v1-profiles", ProfilesView.as_view(), name="list_profile"),
    path("v1-profile/<uuid:pk>", ProfileDetail.as_view(), name="profile_detail")


]