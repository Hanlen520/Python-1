from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'mysite/base.html')

def accounts_profile(request):
    return render(request, 'mysite/accounts_profile.html')
