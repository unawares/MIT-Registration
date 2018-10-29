from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.

from .models import Course
from .models import Registration

def index(request):
    courses = Course.objects.all()
    return render(request, 'courses/main.html', {'courses': courses})

def speakers(request):
    return render(request, 'courses/speakers.html')

def clogout(request):
    logout(request)
    return redirect('/courses/')
    

@login_required
def register(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if Registration.objects.filter(course=course, email=request.user.email).exists():
        return render(request, 'courses/registered.html')
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        Registration.objects.create(course=course, email=request.user.email, name=name, surname=surname)
        return render(request, 'courses/registered.html')
    else:
        return render(request, 'courses/register.html')