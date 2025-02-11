from django.urls import path
from .views import HomeView, BrowseView, RecruiterView

urlpatterns = [
    path('home/', HomeView.as_view(), name="home"),
    path('browse/', BrowseView.as_view(), name="browse"),
    path('recruiter/', RecruiterView.as_view(), name="recruiter"),
]