from django.shortcuts import render, redirect  
from user.forms import UserForm 
from user.models import User  
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = UserForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:
                print("error")  
                pass  
    else:  
        form = UserForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    user = User.objects.all()  
    return render(request,"show.html",{'users':user})  
def edit(request, id):  
    user = User.objects.get(eid=id)  
    return render(request,'edit.html', {'user':user})  
def update(request, id):  
    user = User.objects.get(eid=id)  
    form = UserForm(request.POST, instance = user)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'user': user})  
def destroy(request, id):  
    user = User.objects.get(eid=id)  
    user.delete()  
    return redirect("/show")  