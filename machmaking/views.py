from django.shortcuts import render
from .forms import  MachForm
from django.shortcuts import render, redirect
from .models import  Mach
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def mach_form(request):
    if request.method=="POST":
        form = MachForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mach_form')
        else:
            print(form.errors)
    else:
        form= MachForm()
    return render(request,"mach_form.html",{"form":form})

def mach_list(request):
    machs= Mach.objects.all()
    return render(request, "mach_list.html", {"machs": machs})

# Create your views here.
