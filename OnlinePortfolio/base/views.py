from django.shortcuts import render
from cms.models import *

# Create your views here.

def home(request):
    user = User.objects.get(id=1)
    context = {'user':user}
    return render(request,'home.html',context)

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
    user = User.objects.get(username='admin')
    context = {'user':user}
    return render(request,'Admin/admin.html',context)