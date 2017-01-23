from django.shortcuts import render
from models import Category

def shop(request):
    categories = Category.objects.all()
    return render(request, 'shop/shop.html', {'categories': categories})
