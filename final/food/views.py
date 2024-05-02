from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


# Create your views here.
def main(request):
    logger.info('Main page accessed')
    return render(request, "food/main.html")
