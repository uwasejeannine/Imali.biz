from django.shortcuts import render
from .forms import  LandForm
from django.shortcuts import render, redirect
from .models import Land
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def land_form(request):
    if request.method=="POST":
        form = LandForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('land_form')
        else:
            print(form.errors)
    else:
        form= LandForm()
    return render(request,"land_form.html",{"form":form})

def land_list(request):
    lands= Land.objects.all()
    return render(request, "land_list.html", {"lands": lands})
def land_profile(request,id):
    land= Land.objects.get(id=id)
    return render(request,"land_profile.html",{"land":land})

def edit_land(request, id):
    land= Land.objects.get(id=id)
    if request.method == "POST":
        form=LandForm(request.POST, instance=Land)
        if form.is_valid():
            form.save()
        return redirect("land_profile", id=land.id)
    else:
        form= LandForm(instance=land)
        return render(request,"edit_land.html", {"form":form})
        
def land(request):
    lands=Land.objects.all()
    return render(request,"land.html", {"lands": lands})

def landexplanation(request):
    landexplanations=Land.objects.all()
    return render(request,"landexplanation.html", {"landexplanations": landexplanations})


# Create your views here.