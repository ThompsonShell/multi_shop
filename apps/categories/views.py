
from django.shortcuts import render

from apps.categories.models import Category


def category(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'index.html', context)



