from django.shortcuts import render, get_object_or_404
from .models import Category, Dress

def home(request):
    categories = Category.objects.filter(parent=None).prefetch_related('dresses', 'subcategories__dresses')
    featured = Dress.objects.filter(available=True)[:6]
    dresses = Dress.objects.all() 
    hero_image = Dress.objects.filter(image__isnull=False).exclude(image='').first()
    return render(request, 'app/home.html', {
        'categories': categories,
        'featured': featured,
        'dresses': dresses,   
        'hero_image': hero_image,
    })

def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    dresses = category.dresses.all()
    categories = Category.objects.filter(parent=None)
    return render(request, 'app/category_detail.html', {
        'category': category,
        'dresses': dresses,
        'categories': categories,
    })
