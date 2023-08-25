from django.shortcuts import render
from websites.models import Category, Item

# Create your views here.

def index(request):
    try:
        items = Item.objects.filter(is_sold=False)[0:6]
        categories = Category.objects.all()
        return render(request, 'websites/index.html', {
            'categories': categories,
            'items':items,
        })
    except Exception as err:
        return render(request, 'websites/index.html', {'error':err})

   
    
def about(request):
    try:
        return render(request, 'websites/about.html')
    except Exception as err:
        return render(request, 'websites/about.html', {'error':err})

def service(request):
    try:
        return render(request, 'websites/service.html')
    except Exception as err:
        return render(request, 'websites/service.html', {'error':err})

def gallery(request):
    try:
        return render(request, 'websites/gallery.html')
    except Exception as err:
        return render(request, 'websites/gallery.html', {'error':err})

def faq(request):
    try:
        return render(request, 'websites/faq.html')
    except Exception as err:
        return render(request, 'websites/faq.html', {'error':err})    
    
def contact(request):
    try:
        return render(request, 'websites/contact.html')
    except Exception as err:
        return render(request, 'websites/contact.html', {'error':err})
    

