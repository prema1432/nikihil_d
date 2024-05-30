from django.shortcuts import render


# Create your views here.
def welcome(request):
    context = {}
    context['cityname'] = ["Hyderabad", "Pune", "Mumbai", "Delhi", "Ranchi", "Koklatha", "Biuhar", "Jakarta", "Pali"]
    return render(request, 'welcome.html', context=context)


# a=welcome(name="prrema",lop="opp")

def abouts(request):
    return render(request, 'about.html')


def contactus(request):
    return render(request, 'contactus.html')


def locations(request):
    return render(request, 'locations.html')


def login(request):
    return render(request, 'login.html')
