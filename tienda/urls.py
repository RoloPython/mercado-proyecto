from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("about/", views.about_view, name="about"),
    path("pages/", views.pages_list_view, name="pages_list"),
    path('catalogo/', views.catalogo, name='catalogo'),

]
