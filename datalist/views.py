from django.shortcuts import render,redirect

from datalist.forms import DataForm
from datalist.models import DataList


def data_form(request):
    if request.method=="POST":
        form = DataForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('data_form')
        else:
            print(form.errors)
    else:
        form= DataForm()
    return render(request,"data_form.html",{"form":form})

def data_list(request):
    dataList= DataList.objects.all()
    return render(request, "datalist.html", {"dataList": dataList})



