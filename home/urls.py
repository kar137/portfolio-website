from django.urls import path
from .views import HomeView, BrowseView, RecruiterView, DeveloperView

urlpatterns = [
    path('home/', HomeView.as_view(), name="home"),
    path('browse/', BrowseView.as_view(), name="browse"),
    path('recruiter/', RecruiterView.as_view(), name="recruiter"),
    path('developer/', DeveloperView.as_view(), name="developer"),
    path('stalker/', StalkerView.as_view(), name="stalker"),
    path('adventurer/', AdventurerView.as_view(), name="adventurer"),
]