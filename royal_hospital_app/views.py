from .models import Testimonial
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

# Create your views here.


def index(request):
    testimonials = Testimonial.objects.order_by('-created_at')
    return render(request, 'index.html', {'testimonials': testimonials})

def about(request):
    return render(request, 'about.html')

def departments(request):
    return render(request, 'departments.html')

def contactus(request):
    return render(request, 'contactus.html')

def gallery(request):
    return render(request, 'gallery.html')

def services(request):
    return render(request, 'services.html')

def findadoctor(request):
    return render(request, 'findadoctor.html')

def facilities(request):
    return render(request, 'facilities.html')

def managements(request):
    return render(request, 'managements.html')

def careers(request):
    return render(request, 'careers.html')

def intpatient(request):
    return render(request, 'intpatient.html')

def events(request):
    return render(request, 'events.html')

def make_appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        department = request.POST.get('department')
        date = request.POST.get('date')

        # Compose the message
        subject = 'New Appointment Request'
        message = (
            f'Appointment Details:\n\n'
            f'Name: {name}\n'
            f'Phone: {phone}\n'
            f'Email: {email}\n'
            f'Department: {department}\n'
            f'Preferred Date: {date}'
        )
        recipient_list = ['royalhospitalkollam24@gmail.com']  # Replace with your hospital admin email

        try:
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list, fail_silently=False)
            messages.success(request, 'Your appointment request has been sent successfully!')
        except Exception as e:
            messages.error(request, 'Failed to send appointment request. Please try again later.')
            print(e)

        return redirect('index')  # Reloads the same page
    return render(request, 'index.html')  # Replace with your actual template name

