from django.shortcuts import render,get_object_or_404,redirect
from root.models import Url
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def index(request):
    tikness=0
    try:
        urls = Url.objects.filter(author = request.user, url_show=True )
        for i in urls:
            tikness+=1
        if request.user.subs:
            if request.method =="POST":
                full_url=request.POST.get('full_url')
                if full_url=="":
                    return render(request,"index.html")
                obje = Url.objects.create(
                        full_url=full_url,
                        author=request.user)
                
                
                return render(request,"index.html", {
                    'full_url': obje.full_url,
                    'short_url':obje.short_url
                })

            return render(request,"index.html")
        else:
            if tikness <10 :
                if request.method =="POST":
                    full_url=request.POST.get('full_url')
                    if full_url=="":
                        return render(request,"index.html")
                    obje = Url.objects.create(
                        full_url=full_url,
                        author=request.user)
                    
                    
                    return render(request,"index.html", {
                        'full_url': obje.full_url,
                        'short_url':obje.short_url
                    })

                return render(request,"index.html")
            else:
                messages.success(request,"ABONE DEĞİLSİNİZ EN FAZLA 10 ARL ALABİLİRSİNİZ...")
                messages.success(request,"DAHA FAZLA URL KISALTMAK İÇİN ÖDEME YAPNIZ...")
                return redirect("dashboard")
    except:
        return render(request,"index.html")

@login_required(login_url="/login/")
def dashboard(request):
    
    urls = Url.objects.filter(author = request.user ) 
    print("author id:")
    print(request.user)
    context={
        "urls":urls
    }
    return render(request,"dashboard.html",context)
def allurls(request):
    
    urls = Url.objects.all()
    print("author id:")
    print(request.user)
    context={
        "urls":urls
    }
    return render(request,"dashboard.html",context)

def delete(request,id):
    url= get_object_or_404(Url,id=id,author=request.user)
    url.deleted_date=datetime.datetime.now()
    url.url_show=False
    url.save()
    messages.success(request,"Not Başarı İle Pasifize Edilmiştir....")
    return redirect("dashboard")

def routeurl(request,key):
    # try:
        obj=get_object_or_404(Url,short_url=key)
        if obj.url_show is True:
            obj.click+=1
            obj.save()
            return redirect(obj.full_url)
        else:
            messages.success(request,"Önce Aktif Etmelisiniz..")
            return redirect("index")
    # except:
    #     return redirect("index")

def activateurl(request,id):
    # TODO   orm count ile yapılacak
    url= get_object_or_404(Url,id=id,author=request.user)
    total_url=0
    for urls in url:
        if urls.url_show:
            total_url+=1
    if total_url <10:
        url.url_show=True
        url.save()
        messages.success(request,"Not Başarı İle Aktif Edilmiştir....")
        return redirect("dashboard")
    else:
        messages.success(request,"Daha Fazla Aktif edemezsin aktif Yapazasın....Etmek için Abone olun ")
        return redirect("dashboard")

