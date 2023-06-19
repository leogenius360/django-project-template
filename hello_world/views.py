from django.shortcuts import render
from .models import VisitCounter

# Create your views here.


def index(request):
    """View for the main page of the app"""
    counter = VisitCounter.objects.get_or_create(pk=1)[0]

    # increment the count
    counter.count += 1
    counter.save()

    context = {"visit_counter": counter}
    return render(request, "pages/index.html", context)