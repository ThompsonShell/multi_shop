from django.shortcuts import render

from apps.abouts.models import About


def about(request):
    context = {
        'about': About.objects.first(),
        'page': 'about'
    }
    return render(request, 'about.html',context)

