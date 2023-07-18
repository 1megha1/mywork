from django.shortcuts import redirect, render
from . models import register,gallery
from.form import registerform,LoginForm,Updateform,changepasswordForm
from django.contrib import messages
from django.contrib.auth import logout as logouts

from django.conf import settings
from django.core.mail import send_mail


def index(request):
    return render(request,'index.html')
def registration(request):
    if request.method=='POST':
        form=registerform(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            place=form.cleaned_data['place']
            email=form.cleaned_data['email']
            age=form.cleaned_data['age']
            photo=form.cleaned_data['photo']
            password=form.cleaned_data['password']
            confirmpassword=form.cleaned_data['confirmpassword']
            user=register.objects.filter(email=email).exists()
            if user:
                messages.warning(request,'Email Alredy exist')
                return redirect('/')
            elif password!=confirmpassword:
                messages.warning(request,'Password Mismatch')
            else:
                tab=register(name=name,age=age,place=place,email=email,photo=photo,password=password)
                tab.save()


                subject = 'welcome to abc...'
                message = f'Hi {name}, thank you for registering in abc....'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email, ]
                send_mail( subject, message, email_from, recipient_list )



                messages.success(request,'DATA SAVED')
                return redirect('/')
    else:
        form=registerform()
    return render(request,'registration.html',{'form':form})

def login(request):
    if request.method=='POST':
     form=LoginForm(request.POST)
     if form.is_valid():
         email=form.cleaned_data['email']
         password=form.cleaned_data['password']
         try:
             user=register.objects.get(email=email)
             if not user:
                 messages.warning(request,'Email does not exists')
                 return redirect('/login')
             elif password!=user.password:
                 messages.warning(request,'password incorrect')
                 return redirect('/login')
             else:
                 messages.success(request,'success')
                 return redirect('/home/%s' % user.id)
         except:
              messages.warning(request,'Email or Password incorrect')
              return redirect('/login')
    else:
        form=LoginForm()
        return render(request,'login.html',{'form':form})
    
def home(request,id):
    user=register.objects.get(id=id)
    return render(request,'home.html',{'user':user})
    
def update(request,id):
    user=register.objects.get(id=id)
    if request.method=='POST':
        form=Updateform(request.POST or None,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'Success')
            return redirect('/home/%s' % user.id)
    else:
        form=Updateform(instance=user)
    return render(request,'update.html',{'user':user,'form':form})

def delete(request):
    user=register.objects.get(id=id)
    user.delete()
    messages.success(request,'SUCCESS')
    return redirect('/')

def logout(request):
    logouts(request)
    messages.success(request,'SUCCESS')
    return redirect('/')

def changepassword(request,id):
    user=register.objects.get(id=id)
    if request.method=='POST':
        form=changepasswordForm(request.POST or None)
        if form.is_valid():
            oldpassword=form.cleaned_data['OldPassword']
            newpassword=form.cleaned_data['NewPassword']
            confirmpassword=form.cleaned_data['ConfirmPassword']

            if oldpassword!= user.password:
                messages.warning(request,"incorrect")
                return redirect('/changepassword/%s' % user.id)
            elif oldpassword==newpassword: 
                messages.warning(request, "password similar")
                return redirect('/changepassword/%s' % user.id)
            elif newpassword!=confirmpassword:
                messages.warning(request,"password new")
                return redirect('/'% user.id)
            else:
                user.password=newpassword
                user.save()
                messages.success(request,"change success")
    else:
        form=changepasswordForm()
    return render(request,'changepassword.html',{'user':user, 'form':form})

def signout(request):
    signout(request)
    messages.success(request,"signed out")
    return redirect('/')  

def gallerys(request):
    image=gallery.objects.all()
    return render(request,'gallery.html',{'images':image})

def details(request, id): 
    images=gallery.objects.get(id=id)
    return render(request,'details.html',{'images':images})



            
# Create your views here.
