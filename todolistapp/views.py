from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from todolistapp.models import *
import random
from django.contrib import messages
from datetime import datetime

# Create your views here.

def index(request):
    if 'email' not in request.session:
        return redirect('/login')
    else:
        ins=Task.objects.filter(email=request.session['email'])
        print(ins)
        return render(request,"index.html",{'ins':ins})
    return render(request,'index.html')
    

def loginUser(request):
    if request.method=="POST":
        data=request.POST
        email=data['email']
        password=data['password']
        try:
            user = customertodo.objects.get(email=email)
        except customertodo.DoesNotExist:
            user = None
        if user and user.password==password:
            request.session['email']=email
            request.session['name']=user.fname
            messages.success(request,f"Sign In Successful")
            return redirect("/")
        
    else:
         messages.error(request,"User Or Password Are Incorrect")
         return render(request,"login.html")
         

         
    return render(request,'login.html')

def contact(request):
    if request.method=="POST":
        email=request.POST.get('email')
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        subject=request.POST.get('subject')
        desc=request.POST.get('description')
        contact=Contact(email=email,name=name,phone=phone,subject=subject,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,"Your Message has been sent")
        return redirect('/contact')

    return render(request,"contact.html")

    return render(request,"contact.html")

def signup(request):
    if request.method=="POST":
        data=request.POST
        uid=random.randint(00000,99999)
        email=data['email']
        fname=data['fname']
        lname=data['lname']
        mono=data['no']
        password=data['pass']

        print(uid,email,fname,lname,mono,password)

        customer=customertodo(uid=uid,fname=fname,lname=lname,email=email,mobileno=mono,password=password)
        
        customer.save()
        messages.success(request,"Your Account Registerd Successfully")

        return redirect('/login')
    else:
         return render(request,"signup.html")
    
    return render(request,"signup.html")

def howtouse(request):  
    return render(request,"how_to_use.html")

def teamdet(request):
     return render(request,"team.html")

def logout(request):
    if 'email' in request.session:
        request.session.pop('email')
        return redirect('/login')
    
def addtask(request):
    if request.method=="POST":
        data=request.POST
        tname=data['tname']
        desc=data["desc"]
        cat=data['category']
        status="Not Done"
        email=request.session['email']
        date=datetime.today()
        
        task=Task(tname=tname,desc=desc,status=status,date=date,email=email,category=cat)
        task.save()
        messages.success(request,"Task Added Successfully")
        return redirect('/')

    return render(request,"add_task.html")
    

def delete(request,id):
    print(id)
    queryset=Task.objects.get(id=id)
    queryset.delete()
    messages.success(request,"Task Deleted Successfully")
    return redirect('/')


def taskdone(request,id):
    print(id)
    task = get_object_or_404(Task, id=id)
    task.status = "Done"
    task.save()
    
    messages.success(request,"Task Marked Done Successffully")
    # print(queryset)
    return redirect('/')

def custom_404(request, exception):
    print("Custom 404 view called")
    return render(request, '404.html', status=404)


    