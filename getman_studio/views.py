from django.shortcuts import render
from models import Category, GalleryItem

def gallery(request):
    items = {}
    categories = Category.objects.all();
    print "categories " + str(categories)
    for category in categories:
        try:
            items[category] = GalleryItem.objects.get(category = category)
        except:
            items[category] = None
    return render(request, 'gallery/gallery.html', {'categories': categories, 'items': items})

def workshop(request):
    return render(request, 'workshop/workshop.html')

def contacts(request):
    return render(request, 'contacts/contacts.html')
