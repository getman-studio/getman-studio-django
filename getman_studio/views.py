from django.shortcuts import render

def gallery(request):
    return render(request, 'gallery/gallery.html')

def workshop(request):
    return render(request, 'workshop/workshop.html')

def contacts(request):
    return render(request, 'contacts/contacts.html')
