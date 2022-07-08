from django.shortcuts import render
from .forms import  DeveloperForm
from django.shortcuts import render, redirect
from .models import  Developer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def developer_form(request):
    if request.method=="POST":
        form = DeveloperForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('developer_form')
        else:
            print(form.errors)
    else:
        form= DeveloperForm()
    return render(request,"developer_form.html",{"form":form})

def edit_developer(request, id):
    developer= Developer.objects.get(id=id)
    if request.method == "POST":
        form=DeveloperForm(request.POST, instance=developer)
        if form.is_valid():
            form.save()
        return redirect("edit_developer", id=developer.id)
    else:
        form= DeveloperForm(instance=developer)
        return render(request,"edit_developer.html", {"form":form})
        
def developer(request):
    developers=Developer.objects.all()
    return render(request, "developer.html", {"developers": developers})

def develoxplan(request):
    develoxplan=Developer.objects.all()
    return render(request,"develoxplan.html", {"develoxplan": develoxplan})
