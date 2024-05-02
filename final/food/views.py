from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


# Create your views here.
def main(request):
    logger.info('Main page accessed')
    return render(request, "food/main.html")


def authorization(request):
    return render(request, "food/authorization.html")


def add_receipt(request):
    return render(request, "food/add_receipt.html")

def modify_receipt(request):
    return render(request, "food/modify_receipt.html")

def all_receipt(request):
    return render(request, "food/all_receipt.html")


def get_receipt(request):
    return render(request, "food/get_receipt.html")