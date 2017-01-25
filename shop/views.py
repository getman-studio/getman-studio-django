from django.shortcuts import render
from models import Category, Item

def shop(request):
    categories = Category.objects.all()
    for category in categories:
        category.items = Item.objects.filter(category__id=category.id)
    return render(request, 'shop/shop.html', {'categories': categories})

def checkout(request):
    cartInput = request.POST.get("cart")
    print cartInput
    return render(request, 'shop/checkout.html', {'cart_input': cartInput})
