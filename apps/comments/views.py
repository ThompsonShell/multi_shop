from django.shortcuts import render, redirect
from django.contrib import messages
from sqlparse import split

from apps.comments.forms import CommentCreateForm


def create_comment(request):
    if request.method == "GET":
        return redirect("home-page")
    form = CommentCreateForm(data=request.POST)
    print(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Your comment has been created")
    else:
        messages.error(request, form.errors)

    url = request.META['HTTP_REFERER']
    url = url.split('?')[0]
    return redirect(url)
