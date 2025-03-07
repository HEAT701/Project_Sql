from django.shortcuts import HttpResponse,redirect,render,HttpResponseRedirect
from django.http import  HttpResponse
from Todu_app. models import Todu
from Todu_app.forms import Todo_Form


def add_todu(request):
    data = Todu.objects.all().values()
    if request.method =="POST":
        form = Todo_Form(request.POST)
        if form.is_valid():
           form.save()
        else:
            print('error')
    else:
        form = Todo_Form() 
       
    return render(request,'List_todu.html',{'form':form,'data':data})

def Delete(request,id):
    if request.method =="POST":
        data = Todu.objects.get(id=id)
        data.delete()
        return HttpResponseRedirect('/')
    
def Update(request,id):
    Update_data = Todu.objects.get(id=id)
    if request.method =="POST":
        get = Todo_Form(request.POST,instance=Update_data)
        if get.is_valid():
          get.save()
        return HttpResponseRedirect('/')
    else:
        Update_data = Todu.objects.get(id=id)
        get = Todo_Form(instance=Update_data)
    return render(request,"Update.html",{'id':Update_data,'form':get})