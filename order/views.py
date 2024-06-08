from django.shortcuts import render, redirect

from order.models import my_places


# Create your views here.
def welcome(request):
    context = {}
    context['cityname'] = my_places.objects.all().order_by('-id')
    # context['cityname'] = ["Hyderabad", "Pune", "Mumbai", "Delhi", "Ranchi", "Koklatha", "Biuhar", "Jakarta", "Pali"]
    return render(request, 'welcome.html', context=context)


def create_new_places(request):
    if request.method == 'POST':
        print("request.POST", request.POST)
        my_places.objects.create(location_name=request.POST['location_name'],
                                 location_description=request.POST['location_description'],
                                 age=request.POST['age'])
        return redirect('home')

    return render(request, 'create_new_places.html')


# a=welcome(name="prrema",lop="opp")

def abouts(request):
    return render(request, 'about.html')


def contactus(request):
    return render(request, 'contactus.html')


def locations(request):
    return render(request, 'locations.html')


def login(request):
    return render(request, 'login.html')
