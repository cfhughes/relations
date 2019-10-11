from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        "people" : Person.objects.all(),
        "shoes" : Shoe.objects.all()
    }
    return render(request, 'relate/index.html', context)

def add_shoe(request):
    shoe = Shoe.objects.create(
        color=request.POST['color'],
        brand=request.POST['brand'])
    print("Post: " + str(type(request.POST.get('person_id'))))
    for owner in request.POST.getlist('person_id'):
        print(owner)
        shoe.owners.add(Person.objects.get(id=owner))
    shoe.save()
    return redirect("/")

def add_person(request):
    person = Person.objects.create(name=request.POST['name'])
    person.save()
    return redirect("/")