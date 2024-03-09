from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')
    
def abouts(request):
    return render(request,'About.html')
    
def resume(request):
    return render(request,'resume.html')

def contact(request):
    return render(request,'contact.html')

def gallery(request):
    return render(request,'gallery.html')

def project(request):
    return render(request,'project.html')

def admin(request):
    return render(request,'Admin/admin.html')