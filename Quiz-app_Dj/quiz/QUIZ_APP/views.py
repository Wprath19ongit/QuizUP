from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import USER
# from .forms import usersForm
# from django.contrib.auth.models import User


def home_view(request,*args,**kwargs):
    return render(request,"home.html",{})

def sign_in_view(request,*args,**kwargs):
    return render(request,"sign_in.html",{})

def sign_up_view(request,*args,**kwargs):
    return render(request,"sign_up.html",{})

def about_view(request,*args,**kwargs):
    return render(request,"about.html",{})



def user_options_view(request,*args,**kwargs):
    if(request.method=="POST"):

        username = request.POST.get('uname')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pword = request.POST.get('pword1')
        pword2 = request.POST.get('pword2')
        reg_time = datetime.datetime.now()

        # check errors
        # if(username not in db.USER.findOne({username: username})):
        ins = USER.objects.create(
            first_name = fname,
            last_name = lname,
            username = username,
            email = email,
            log_in = datetime.datetime.now(),
            reg_time = reg_time,
            password = pword
        )

        return render(request,"sign_in.html",{})
    else:
        return redirect(request,"home.html",{})
       
        # ins = User(username=username,email=email,password = pword)
        # ins.first_name=fname
        # ins.last_name=lname
        # ins.reg_time = reg_time
        # ins.save()

        # ins.success(request, "You have successfully registed")





def user_options_view2(request,*args,**kwargs):
    if(request.method=="POST"):

        username = request.POST.get('uname')
        pword = request.POST.get('pword1')
        login_time = datetime.datetime.now()

        
    #     user = authenticate(username=username, password=pword)
        
    #     if user is not None:
    #         login(request, user)
    #         fname = user.first_name
            
    #         return render(request, "user_options.html",{"fname":fname})
    #     else:
    #         messages.error(request, "Bad Credentials!!")
    #         return redirect('sign_in.html')
    
    #     # ins.success(request, "You have successfully registed")

        return render(request,"user_options.html",{})
    else:
        return redirect(request,"home.html",{})



def create_quiz_view(request, *args, **kwargs):
    return render(request, "create_quiz.html",{})

def take_quiz_view(request, *args, **kwargs):
    return render(request, "take_quiz.html",{})
