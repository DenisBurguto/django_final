from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
import logging

logger = logging.getLogger(__name__)


# Create your views here.
def main(request):
    logger.info('Main page accessed')
    return render(request, "food/main.html")


def authorization(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            logger.info(f'New loging {user.username}')
            return redirect('main')
    else:
        form = LoginForm()
    return render(request, 'food/authorization.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            logger.info('New registration')
            return redirect('main')
    else:
        form = RegistrationForm()
    return render(request, 'food/authorization.html', {'form': form})


def user_logout(request):
    logout(request)
    logger.info('logout')
    return redirect('main')


def add_receipt(request):
    return render(request, "food/add_receipt.html")


def modify_receipt(request):
    return render(request, "food/modify_receipt.html")


def all_receipt(request):
    return render(request, "food/all_receipt.html")


def get_receipt(request):
    return render(request, "food/get_receipt.html")
