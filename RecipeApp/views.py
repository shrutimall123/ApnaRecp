from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Corrected the template name


def contact(request):
    return render(request, 'contact.html')


def contributor(request):
    return render(request, 'contributor.html')


def gallery(request):
    return render(request, 'gallery.html')


def icons(request):
    return render(request, 'icons.html')


def services(request):
    return render(request, 'services.html')


def signup(request):
    return render(request, 'signup.html')


def typography(request):
    return render(request, 'typography.html')


def error(request):
    return render(request, '404.html')


def about(request):
    return render(request, 'about.html')
