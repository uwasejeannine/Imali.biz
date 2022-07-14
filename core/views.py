from django.shortcuts import render,redirect


def home(request):
    return render(request,"home.html", {"home": home})

def data(request):
    return render(request,"data.html", {"data": data})




