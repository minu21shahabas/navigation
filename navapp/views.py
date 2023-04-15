from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request,'home.html')
def sign(request):
    return render(request,'signup.html')
def logins(request):
    return render(request,'login.html')
#@login_required(login_url='logins')
def out(request):
    if 'uid' in request.session:
    #if request.user.is_authenticated:
        #return render(request,'about.html')    
    #return render(request,'login.html')

        return render(request,'about.html')
    return render(request,'login.html')
    #if request.user.is_authenticated:
        #return render(request,'about.html')
    #return render(request,'login.html')
#@login_required(login_url='logins')    
def back(request):
    request.session['uid']=""
    #if request.user.is_authenticated:
       # auth.logout(request)
    auth.logout(request)
    return redirect('home')
def create(request):
    if request.method=="POST":
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        username=request.POST['uname']
        email=request.POST['email']
        password=request.POST['pass']
        rpassword=request.POST['pass1']
        
        if password==rpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"This username already exist!!!!")
                return redirect('sign')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username,
                    password=password )
                user.save()
                print("success...!")
        else:
            messages.info(request,"password doesnot match...!")
            print("Password is not matching")
            return redirect('sign')
        return redirect('logins')
    else:
        return render(request,'signup.html')
def log(request):
    if request.method=='POST':
        usernme=request.POST['user']
        print(usernme)
        password=request.POST['pass']
        print(password)
        user=auth.authenticate(username=usernme,password=password)
        request.session["uid"]=user.id
        if user is not None:
            #if user.is_staff:
                auth.login(request,user)
                messages.info(request,f'welcome {usernme}')
                return redirect('out')
        else:
            messages.info(request,'invalid username or password.Try again!!')
            return redirect('logins')
    else:
        return render(request,'login.html')
def super(request):
    return render(request,'admin.html')



