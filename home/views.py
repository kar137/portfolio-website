from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from .models import FavoriteMovies, Projects


# Create your views here.

class BrowseView(TemplateView):
    template_name = "home/browse.html"

class HomeView(TemplateView):
    template_name = "home/home.html"

class RecruiterView(ListView):
    model = Projects
    template_name = "home/recruiter.html"
    context_object_name = "projects"

    def get_queryset(self):
        return Projects.objects.all().order_by('-date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Recruiter'
        return context
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send email
        try:
            send_mail(
                subject= f"New message from {name}",
                message= f"Name: {name}\nEmail: {email}\nMessage: {message}",
                from_email= settings.EMAIL_HOST_USER,
                recipient_list= [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            return JsonResponse({'success': True, 'message': 'Your message has been sent successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': 'Failed to send message. Please try again later.'})
        

class DeveloperView(TemplateView):
    template_name = "home/developer.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':'Developer'})
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        try:
            send_mail(
                subject= f"New message from {name}",
                message= f"Name: {name}\nEmail: {email}\nMessage: {message}",
                from_email= settings.EMAIL_HOST_USER,
                recipient_list= [settings.EMAIL_HOST_USER],
                fail_silently= False,
            )
            return JsonResponse({'success': 'True', 'message': 'Your message has been sent successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': 'Failed to send message. Please try again later.'})

class StalkerView(ListView):
    model = FavoriteMovies
    template_name = "home/stalker.html"
    context_object_name = "movies"
    
    def get_queryset(self):
        return FavoriteMovies.objects.all().order_by('-rating')[:3]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Stalker'
        return context
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        try:
            send_mail(
                subject= f"New message from {name}",
                message= f"Name: {name}\nEmail: {email}\nMessage: {message}",
                from_email= settings.EMAIL_HOST_USER,
                recipient_list= [settings.EMAIL_HOST_USER],
                fail_silently= False,
            )
            return JsonResponse({'success': 'True', 'message': 'Your message has been sent successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': 'Failed to send message. Please try again later.'})

class AdventurerView(ListView):
    model = FavoriteMovies
    template_name = "home/adventurer.html"
    context_object_name = "movies"

    def get_queryset(self):
        return FavoriteMovies.objects.all().order_by('-rating')[:3]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Adventurer'
        return context
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        try:
            send_mail(
                subject= f"New message from {name}",
                message= f"Name: {name}\nEmail: {email}\nMessage: {message}",
                from_email= settings.EMAIL_HOST_USER,
                recipient_list= [settings.EMAIL_HOST_USER],
                fail_silently= False,
            )
            return JsonResponse({'success': 'True', 'message': 'Your message has been sent successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': 'Failed to send message. Please try again later.'})

