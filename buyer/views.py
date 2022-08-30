from django.shortcuts import render
from .forms import  BuyerForm
from django.shortcuts import render, redirect
from .models import Buyer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def buyer_form(request):
    if request.method=="POST":
        form = BuyerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('buyer_form')
        else:
            print(form.errors)
    else:
        form= BuyerForm()
    return render(request,"buyer_form.html",{"form":form})

def buyer_list(request):
    buyers= Buyer.objects.all()
    return render(request, "buyer_list.html", {"buyers": buyers})

def buyer_profile(request,id):
    buyer= Buyer.objects.get(id=id)
    return render(request,"buyer_profile.html",{"buyer":buyer})

def edit_buyer(request, id):
    buyer= Buyer.objects.get(id=id)
    if request.method == "POST":
        form=BuyerForm(request.POST, instance=buyer)
        if form.is_valid():
            form.save()
        return redirect("buyer_profile", id=buyer.id)
    else:
        form= BuyerForm(instance=buyer)
        return render(request,"edit_buyer.html", {"form":form})
        
def buyer(request):
    buyers=Buyer.objects.all()
    return render(request,"buyer.html", {"buyers": buyers})

def buyerexplan(request):
    buyerexplan=Buyer.objects.all()
    return render(request,"buyerexplan.html", {"buyerexplan": buyerexplan})
from django.contrib import messages

def my_view(request):
       if form.is_valid():
          messages.success(request, 'Form submission successful')


# Create your views here.