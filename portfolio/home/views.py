from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class BrowseView(TemplateView):
    template_name = "home/browse.html"

class HomeView(TemplateView):
    template_name = "home/home.html"

class RecruiterView(TemplateView):
    template_name = "home/recruiter.html"

