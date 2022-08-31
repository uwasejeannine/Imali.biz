from django.shortcuts import render
from .forms import  InvestorForm
from django.shortcuts import render, redirect
from .models import Investor
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def investor_form(request):
    if request.method=="POST":
        form = InvestorForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('investor_form')
        else:
            print(form.errors)
    else:
        form= InvestorForm()
    return render(request,"investor_form.html",{"form":form})

def investor_list(request):
    investors= Investor.objects.all()
    return render(request, "investor_list.html", {"investors": investors})
def investor_profile(request,id):
    investor=Investor.objects.get(id=id)
    return render(request,"investor_profile.html",{"investor":investor})

def edit_investor(request, id):
    inverstor= Investor.objects.get(id=id)
    if request.method == "POST":
        form=InvestorForm(request.POST, instance=inverstor)
        if form.is_valid():
            form.save()
        return redirect("investor_profile", id=inverstor.id)
    else:
        form=InvestorForm(instance=inverstor)
        return render(request,"edit_investor.html", {"form":form})
        
def inverstor(request):
    investors=Investor.objects.all()
    return render(request,"investor.html", {"investors": investors})

def investorexplanation(request):
    invdetails=Investor.objects.all()
    return render(request,"invdetails.html", {"invdetails":invdetails})


def documentation(request):
    document=Investor.objects.all()
    return render(request,"docmentation.html", {"document":document})


# Create your views here.