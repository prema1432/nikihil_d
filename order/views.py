from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from order.forms import my_placesform, MyLoginForm
from order.models import my_places



def login_view(request):
    context={}
    if request.method == 'POST':
        form = MyLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) # valid crednatils
            if user is not None:
                login(request, user) # logging
                return redirect('home')
            else:
                context["error"]="Invalid CreateUser"
                context["form"] = MyLoginForm

        else:
            context["error"] = "Invalid CreateUser"
            context["form"] = MyLoginForm

    else:
        context["form"] = MyLoginForm
    return render(request,'login.html',context)



def logout_view(request):
    logout(request)
    return redirect('home')

# Create your views here.
def welcome(request):
    context = {}
    context['cityname'] = my_places.objects.all().order_by('-id')
    # context['cityname'] = ["Hyderabad", "Pune", "Mumbai", "Delhi", "Ranchi", "Koklatha", "Biuhar", "Jakarta", "Pali"]
    return render(request, 'welcome.html', context=context)


def get_place(request, id):
    context = {}
    try:
        context['cityname'] = my_places.objects.get(id=id)
    except my_places.DoesNotExist:
        context['cityname'] = None
        context['error'] = "You entrr wrong id."
    return render(request, 'get_place.html', context=context)


def get_place_update(request, id):
    context = {}
    get_place = get_object_or_404(my_places, id=id)
    form = my_placesform( instance=get_place)

    if request.method == 'POST':
        form = my_placesform(request.POST, request.FILES, instance=get_place)

        if form.is_valid:
            form.save()
            return redirect('home')
        else:
            print("errors 897798",form.errors)
            context["errors"] = form.errors
            return render(request, 'create_new_places.html', context=context)

    context['form'] = form

    return render(request, 'create_new_places.html', context=context)


# def create_new_places(request):
#     if request.method == 'POST':
#         print("request.POST", request.POST)
#         my_places.objects.create(location_name=request.POST['location_name'],
#                                  location_description=request.POST['location_description'],
#                                  age=request.POST['age'])
#         return redirect('home')
#
#     return render(request, 'create_new_places.html')

def create_new_places(request):
    context = {}
    form = my_placesform(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        context["errors"] = form.errors
    context['form'] = form

    return render(request, 'create_new_places.html', context=context)


# a=welcome(name="prrema",lop="opp")


def place_delete(request,id):
    places = get_object_or_404(my_places, id=id)
    places.delete()
    return redirect('home')

@login_required
def abouts(request):
    return render(request, 'about.html')


def contactus(request):
    return render(request, 'contactus.html')


def locations(request):
    return render(request, 'locations.html')


# def login(request):
#     return render(request, 'login.html')
