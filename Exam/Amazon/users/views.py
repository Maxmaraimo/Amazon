import logging
from math import e

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ProfileForm, UserForm, UserUpdateForm
from .usecases import *

import smtplib
from email.mime.text import MIMEText


log = logging.getLogger(__name__)


def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'registration/create_user.html', context)

    context = {'form': UserForm()}
    return render(request, 'registration/create_user.html', context)

def shopnow(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'registration/shop_now.html', context)

    context = {'form': UserForm()}
    return render(request, 'registration/shop_now.html', context)
    
def ExploreMore(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'registration/explore.html', context)

    context = {'form': UserForm()}
    return render(request, 'registration/explore.html', context)

def SeeAllDeal(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'registration/see_all_deals.html', context)

    context = {'form': UserForm()}
    return render(request, 'registration/see_all_deals.html', context)


def SeeMore(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'registration/see_more.html', context)

    context = {'form': UserForm()}
    return render(request, 'registration/see_more.html', context)


def laptops(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'registration/laptops.html', context)

    context = {'form': UserForm()}
    return render(request, 'registration/laptops.html', context)

def Toys(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'registration/toys.html', context)

    context = {'form': UserForm()}
    return render(request, 'registration/toys.html', context)


def Perfume(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'registration/perfume.html', context)

    context = {'form': UserForm()}
    return render(request, 'registration/perfume.html', context)

def AtTheMoment(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'registration/atthemoment.html', context)

    context = {'form': UserForm()}
    return render(request, 'registration/atthemoment.html', context)

def ProductBook(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'registration/books.html', context)

    context = {'form': UserForm()}
    return render(request, 'registration/books.html', context)

def ProductDrinks(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'registration/drinks.html', context)

    context = {'form': UserForm()}
    return render(request, 'registration/drinks.html', context)

def CocaCola(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'registration/cocacola.html', context)

    context = {'form': UserForm()}
    return render(request, 'registration/cocacola.html', context)


def Pepsi(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'registration/pepsi.html', context)

    context = {'form': UserForm()}
    return render(request, 'registration/pepsi.html', context)


def Sprite(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'registration/sprite.html', context)

    context = {'form': UserForm()}
    return render(request, 'registration/sprite.html', context)


@login_required
def profile(request):

    if request.method == 'POST':
        p_form = ProfileForm(request.POST,
                             instance=request.user.profile,
                             files=request.FILES)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            user = u_form.save(commit=True)
            profile = p_form.save(commit=True)
            messages.success(request,
                             f"Your account has been updated!")
            return redirect('profile')
        else:
            context = {
                "u_form": u_form,
                "p_form": p_form,
            }
            return render(request, 'profile.html', context)

    context = {
        'u_form': UserUpdateForm(instance=request.user),
        'p_form': ProfileForm(instance=request.user.profile)
    }
    return render(request, 'profile.html', context)


def send_email(recipient, subject, body):
    message = MIMEText(body, 'plain')
    message['From'] = 'ozodbekmahmaraimov16@gmail.com'
    message['To'] = "davlatbemmiya@gmail.com"
    message['Subject'] = subject

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('ozodbekmahmaraimov16@gmail.com', 'ozod2809')
        server.sendmail('ozodbekmahmaraimov16@gmail.com', recipient, message.as_string())

