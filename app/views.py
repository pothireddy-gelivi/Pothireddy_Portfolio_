from django.shortcuts import render, redirect
from .models import Resume, Skill, Project, Contact

def home(request):
    resume = Resume.objects.last()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    return render(request, 'home.html', {
        'resume': resume,
        'skills': skills,
        'projects': projects
    })

def contact(request):
    if request.method == 'POST':
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            message=request.POST['message']
        )
        return redirect('home')
    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def resume(request):
    
    return render(request, 'resume.html')