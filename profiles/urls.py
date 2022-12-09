from django.urls.conf import path
from profiles.views import index, profile

urlpatterns = [
    path("", index, name="profiles_index"),
    path("<str:username>/", profile, name="profile"),
]
