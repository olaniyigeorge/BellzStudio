"""
URL configuration for BellzStudio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from BellzStudio import settings

from django.conf.urls.static import static # type: ignore

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('main.urls')),
    path("dev-stories/", include('stories.urls')),
    path("notes/", include('notes.urls')),

    # ---- API ROUTES ----
    path("api/accounts/", include('main.apiUrls')),
    path("api/notes/", include('notes.apiUrls')),

    
] + static(settings.STATIC_URL)
# + static(settings.STATIC_URL)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)