from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request=request, template_name='contact.html',context={'page':'contact'})
