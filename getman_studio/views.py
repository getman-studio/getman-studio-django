from django.shortcuts import render
from models import Category, GalleryItem, Article

def gallery(request):
    items = {}
    categories = Category.objects.all();
    print "categories " + str(categories)
    for category in categories:
        try:
            items[category] = GalleryItem.objects.get(category = category)
        except:
            items[category] = []
        print str(category) + str(items)
    return render(request, 'gallery/gallery.html', {'categories': categories, 'items': items})

def workshop(request):
    articles = Article.objects.all()
    return render(request, 'workshop/workshop.html', { 'articles': articles })

def contacts(request):
    return render(request, 'contacts/contacts.html')
