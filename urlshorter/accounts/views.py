from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login,authenticate,logout
from django.urls import reverse
from accounts.forms import Loginform,Registerform
from django.contrib import messages


User = get_user_model()

def loginuser(request):
   

    if request.method=="POST":
        form=Loginform(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user =  authenticate(username=username,password=password)
        

            if user is None:
                messages.info(request,"Kullanıcı veya Parola hatalı....")
                
                return render(request,"login.html",context)
            messages.success(request,"Başarıyla Giriş Yapıldı...")
            login(request,user)
            return redirect("index")
    else:
        form=Loginform()
    # form=Loginform(request.POST or None) bu da doğru ama diğeri daha doğru çünkü POST boş gelirse none olarak algılar
    context={
        "form":form
    }
    return render(request,"login.html",context)

def register(request):
    if request.method=="POST":
       form = Registerform(request.POST)
       if form.is_valid():
           username=form.cleaned_data.get("username")
           password=form.cleaned_data.get("password")
           newUser=User(username = username)
           newUser.set_password(password)
           newUser.save()
           login(request,newUser)
           messages.success(request,"Kayıt işlemi Başarılı")
           messages.info(request,"Kayıt işlemi Başarılı")
           return redirect("index")
       context ={
            "form": form
        }
       return render(request,"register.html",context)
           
    else:
        form=Registerform()
        context ={
            "form": form
        }
        return render(request,"register.html",context)

def logoutuser(request):
        logout(request)
        messages.success(request,"Başarı ile çıkış sağladınız....")
        return redirect("index")

"""def subs(request):
    if request.user.is_superuser:
        messages.success(request,"zaten üyeliğiniz bulunmaktadır....")
        return redirect("index")
    else:
        messages.success(request,"Tebrikler Üye oldunuz.......")
        user =User.objects.filter(id=request.user.id).first()
        user.is_superuser =True"""

def activatesubs(request):
    print(request.user.subs)
    if request.user.subs:
        print(request.user.subs)
        return redirect(reverse("dashboard"))
    else:  
        # get_object_or_404 kullanmazsam hüseyin bana kızar azıcıks
        user =User.objects.filter(id=request.user.id).first()
        user.subs =True
        user.save()
        print(request.user.subs)
        messages.success(request,".........TEBRİKLER ÜYE OLDUNUZ..........")
        return redirect("dashboard")
        

    
