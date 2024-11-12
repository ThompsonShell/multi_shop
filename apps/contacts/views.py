from django.shortcuts import render, redirect
from django.contrib import messages

from apps.contacts.forms import ContactCreateForm


def contact(request):
    return render(request=request, template_name='contact.html',context={'page':'contact'})


def create_comment(request):
    if request.method == "GET":
        return redirect("home-page")
    form = ContactCreateForm(data=request.POST)
    print("==========")
    print(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Your message has been created")
    else:
        print("===========================")
        messages.error(request, form.errors)

    url = request.META['HTTP_REFERER']
    url = url.split('?')[0]
    return redirect(url)
