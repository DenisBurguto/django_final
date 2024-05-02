from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, LoginForm, ReceiptForm, CategoryForm, RecipeSearchForm
from .models import Receipt
import logging

logger = logging.getLogger(__name__)


# Create your views here.
def main(request):
    recent_receipts = Receipt.objects.all()[:5]
    logger.info('Main page accessed')
    return render(request, "food/main.html", {'recent_receipts': recent_receipts})


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
    if request.method == 'POST':
        form = ReceiptForm(request.POST, request.FILES)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.author = request.user
            receipt.save()
            logger.info(f'Added receipt by {receipt.author}')
            return redirect('main')
    else:
        form = ReceiptForm()
    return render(request, 'food/add_receipt.html', {'form': form})


def modify_receipt(request):
    return render(request, "food/modify_receipt.html")


def all_receipt(request):
    recipes = Receipt.objects.all()
    return render(request, "food/all_receipt.html", {'recipes': recipes})


def get_receipt(request):
    if request.method == 'GET':
        form = RecipeSearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            recipes = (Receipt.objects.filter(name__icontains=search_query) | Receipt.objects.filter(
                description__icontains=search_query))
            return render(request, 'food/recipe_search_results.html',
                          {'recipes': recipes, 'search_query': search_query})
    else:
        form = RecipeSearchForm()
    return render(request, "food/get_receipt.html", {'form': form})


def receipt_detail(request, receipt_id):
    receipt = get_object_or_404(Receipt, pk=receipt_id)
    return render(request, 'food/receipt_detail.html', {'receipt': receipt})


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            logger.info('new category created')
            return redirect('main')
    else:
        form = CategoryForm()
    return render(request, 'food/create_category.html', {'form': form})
