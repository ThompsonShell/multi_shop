from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, template_name='index.html')


def shop(request):
    return render(request=request, template_name='shop.html',context={'page':'shop'})

