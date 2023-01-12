from django.contrib import admin
from django.urls import path, include

from .views import views

handler404 = 'oc_lettings_site.views.my_custom_page_not_found_view'

urlpatterns = [
    path("", views.index, name="index"),
    path("profiles/", include("profiles.urls")),
    path("lettings/", include("lettings.urls")),
    path("admin/", admin.site.urls),
]
