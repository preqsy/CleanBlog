from django.shortcuts import render, redirect
from .models import *


def index(request):
    home = Home.objects.order_by('-time')[0:4]
    return render(request, 'index.html', {'home': home})


def next(request):
    home = Home.objects.order_by('-time')[4:8]
    return render(request, 'newindex.html', {'home': home})


def next_page(request):
    home = Home.objects.order_by('-time')[8:12]
    return render(request, 'newindex.html', {'home': home})


def post(request, pk):
    home = Home.objects.get(id=pk)
    return render(request, 'post.html', {'home': home})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        new_contact = Contact(name=name, phone=phone, email=email, message=message)
        new_contact.save();
        return redirect('contact')
    else:
        return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')
