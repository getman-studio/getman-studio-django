from django.shortcuts import render
from models import Category, GalleryItem, Article, WorkshopParallaxItem

def gallery(request):
    categories = Category.objects.filter(active=True);
    gitems = GalleryItem.objects.all();
    return render(request, 'gallery/gallery.html', {'categories': categories, 'items': gitems})

def workshop(request):
    articles = Article.objects.all()
    parallaxItems = list(WorkshopParallaxItem.objects.all())

    firstParallax = None
    lastParallax = None
    if (len(parallaxItems) >= 1):
        firstParallax = parallaxItems.pop(0)
    if (len(parallaxItems) >= 2):
        lastParallax = parallaxItems.pop(-1)

    x = 0
    for article in articles:
        i = x + 1
        if i % 2 == 0 and i < articles.count() and len(parallaxItems) > i / 2:
            article.parallax = parallaxItems[i / 2]
        x += 1

    print str(articles)
    return render(request, 'workshop/workshop.html', { 'firstParallax': firstParallax, 'lastParallax': lastParallax, 'articles': articles })

def contacts(request):
    return render(request, 'contacts/contacts.html')

def shop(request):
    return render(request, 'shop/shop.html')
