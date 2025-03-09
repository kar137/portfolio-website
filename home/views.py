from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse


# Create your views here.

class BrowseView(TemplateView):
    template_name = "home/browse.html"

class HomeView(TemplateView):
    template_name = "home/home.html"

class RecruiterView(TemplateView):
    template_name = "home/recruiter.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': 'Recruiter'})
    
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

class StalkerView(TemplateView):
    template_name = "home/stalker.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':'Stalker'})
    
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

class AdventurerView(TemplateView):
    template_name = "home/adventurer.html"
    
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':'Adventurer'})
    
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

