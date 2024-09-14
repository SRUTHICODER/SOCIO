from django.template import loader
from audioop import reverse
from time import time
from unittest import result
from urllib import response
from django.http import  HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from mysqlx import Result
from .models import *
import datetime
from json import dumps
from .forms import *

def set_cookie(response, key, value, days_expire=30):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(
        datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
        "%a, %d-%b-%Y %H:%M:%S GMT",
    )
    response.set_cookie(
        key,
        value,
        max_age=max_age,
        expires=expires
    )

def login(request):
    if 'email' in request.COOKIES and 'pw' in request.COOKIES:
        data=user.objects.filter(u_mailid=request.COOKIES['email'],pswd=request.COOKIES['pw'])
        if data:
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request,"login.html")
    else:
        return render(request,"login.html")

def verify(request):
    if request.method=="POST":
        emailid=request.POST["email"]
        password=request.POST["pw"]
        data=user.objects.filter(u_mailid=emailid,pswd=password)
    if data :
        response= HttpResponseRedirect(reverse("home"))
        set_cookie(response,'email', emailid)
        set_cookie(response,'pw', password)
        return response
    else:
        return HttpResponseRedirect(reverse("login"))

def logout(request):
    response=HttpResponseRedirect(reverse('login'))
    response.delete_cookie("email")
    response.delete_cookie("pw")
    return response


def home(request):
    if 'email' in request.COOKIES and 'pw' in request.COOKIES:
        data=user.objects.filter(u_mailid=request.COOKIES['email'],pswd=request.COOKIES['pw'])
        if data:
            return render(request,"home.html")
        else:
            return HttpResponseRedirect(reverse("login"))
    else:
        return HttpResponseRedirect(reverse("login"))


            
def Request(request):
    if 'email' in request.COOKIES and 'pw' in request.COOKIES:
        data=user.objects.filter(u_mailid=request.COOKIES['email'],pswd=request.COOKIES['pw'])
        if data:
            d=user.objects.values('u_id', 'u_name')
            print(d.values)
            # d=list(d.values())
            # d=dumps(d,default=str)
            return render(request,"Request.html",{'d':d})
        else:
            return render(request,"login.html")
    else:
        return render(request,"login.html")
    



def registration(request):
    if request.method=="POST":
        form=registerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form=registerForm()
    return render(request,"registration.html",{'form':form})

    
def profile(request):
    if 'email' in request.COOKIES and 'pw' in request.COOKIES:
        data=user.objects.filter(u_mailid=request.COOKIES['email'],pswd=request.COOKIES['pw'])
        if data:
            m=request.COOKIES['email']
            data1=user.objects.all()
            for i in data1:
                if i.u_mailid == m:
                    u_name=i.u_name
                    u_mailid=i.u_mailid
                    hobby=i.hobby
                    address=i.address
                    profession=i.profession
                    dob=i.dob
                    education=i.education
                    phone_no=i.phone_no
                    if(i.pic):
                        pic=i.pic
                    return render(request,"profile.html",{
                        "name":u_name,
                        "mailid":u_mailid,
                        "hobby":hobby,
                        "addr":address,
                        "prof":profession,
                        "dob":dob,
                        "edu":education,
                        "ph_no":phone_no,
                        "pic":pic
                    })
            return HttpResponseRedirect(reverse('login'))

def pro1(request,id):
     if 'email' in request.COOKIES and 'pw' in request.COOKIES:
        data=user.objects.filter(u_mailid=request.COOKIES['email'],pswd=request.COOKIES['pw'])
        if data:
            d1=user.objects.filter(u_id=id)
            if d1:
                data1=user.objects.all()
                for i in data1:
                    if i.u_id == id:
                        u_id=i.u_id
                        u_name=i.u_name
                        u_mailid=i.u_mailid
                        hobby=i.hobby
                        address=i.address
                        profession=i.profession
                        dob=i.dob
                        education=i.education
                        phone_no=i.phone_no
                        pic=i.pic
                        return render(request,"pro1.html",{
                            "u_id":u_id,
                            "name":u_name,
                            "mailid":u_mailid,
                            "hobby":hobby,
                            "addr":address,
                            "prof":profession,
                            "dob":dob,
                            "edu":education,
                            "ph_no":phone_no,
                            "pic":pic
                        })
        return HttpResponseRedirect(reverse('login'))

def cre(request,id):
    if 'email' in request.COOKIES and 'pw' in request.COOKIES:
        data=user.objects.filter(u_mailid=request.COOKIES['email'],pswd=request.COOKIES['pw'])
        if data:
            data2=user.objects.filter(u_id=id)
            # m=request.COOKIES['email']
            # data=user.objects.all()
            # for x in data:
            #     if x.u_mailid==m :
            #         iid=x.u_id
            #         break
            # data1=user.objects.filter(u_id=iid)
            obj1=Req.objects.create(reqsender_id=data[0],reqreceiver_id=data2[0],time=datetime.datetime.now())
            Req.save(obj1)
            response= HttpResponseRedirect(reverse('home'))
            return response
        else:
            return HttpResponseRedirect(reverse('login'))
        

    #  ans_text=request.POST["ansBox"]
    #                 img_link=request.POST["lin"]
    #                 data1=question.objects.filter(q_id=q_id)
    #                 data15=ques_pbna.objects.get(q_id=data1[0])
    #                 # print(data15.values())
    #                 data15.sat = 2
    #                 data15.save()





    