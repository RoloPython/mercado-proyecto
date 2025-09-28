from django.urls import path, include
from . import views

urlpatterns = [
    # las urls de autenticación (login/logout) estarán en /accounts/login/ etc.
    path("", include("django.contrib.auth.urls")),
    path("signup/", views.signup_view, name="signup"),
    path("profile/", views.profile_view, name="profile"),
]

