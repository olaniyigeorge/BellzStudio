from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from notes.models import Reader
from .models import User
from django.contrib.auth import authenticate, login, logout
from main.forms import SignUpForm
# Create your views here.



def index(request):
    user = request.user
    
    try:
        user_profile = User.objects.get(email=user)
        print(user_profile.first_name)    
    except:
        user_profile = None
    
    return render(request, 'main/index.html', {'user': user_profile})


def about(request):

    return render(request, 'main/about-us.html', {})


def contact(request):

    destination = 'twitter'


    return HttpResponseRedirect(reverse(
                        "main:contact_type", args=(destination,)
                        ))
    # return render(request, "main/contact-us.html", {})


def contactType(request, destination):

    print(destination)

    contacts = {
        "twitter": {
            'link': 'https://twitter.com/imoctborn',
            'username': '@imoctborn',
            'icon_link': 'images/twit.png'               
        },
        "linkedin": {
            'link': 'https://linkedin.com/in/abeleje-olaniyi',
            'username': 'Abeleje Olaniyi',
            'icon_link': 'images/linkedin_pfp.jpeg'               
        },
        "email": {
            'link': 'mailto:olaniyigeorge77@gmail.com',
            'username': 'olaniyigeorge77@gmail.com',
            'icon_link': 'images/my-twitter.png'               
        },
    }

    info = contacts[destination]
    print(info)

    return render(request, "main/contact-des.html", {'destination': destination, 'info': contacts[destination]})




# USER MANGEMENT


def profile(request):
    user = request.user
    if not user.is_authenticated:
        user = None
        return render(request, 'main/my-profile.html', {"user": user})
        #user_profile = Profile.objects.get(user=user)
    
    return render(request, 'main/my-profile.html', {"user": user})




# NETWORK


def newtork(request):
    user = request.user
    if not user.is_authenticated:
        user = None
        return render(request, 'main/not.html', {"user": user})
        #user_profile = Profile.objects.get(user=user)
    
    return render(request, 'main/my-profile.html', {"user": user})



def signUp(request):

    try:
        role = request.GET['role']
        # print("Tag Param: ", request.GET['tag'])
    except Exception as e:
        role = None
        # print("Error: ", e)
    # role = request.GET['role'] or "" 

    print("Role: ", role)

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        # Role
        reader = request.POST['reader']
        print("Email:", email)
        print("Password:", password)
        print("Reader:", reader)


        if password != password_confirmation:
            return HttpResponseRedirect(reverse("main:sign-up"))    
        
        try:
            user, created = User.objects.get_or_create(email=email, password=password)
            if reader == 'on':
                reader = Reader.objects.get_or_create(user=user)

        except:
            return HttpResponseRedirect(reverse("main:sign-up"))
                
        try:

            # Get username and password for authentication
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')

            # Log user in with username and raw password
            user = authenticate(username=email, password=raw_password)
            login(request, user)

            return HttpResponseRedirect(reverse("main:index"))     
        except Exception as e:
            return HttpResponseRedirect(reverse("main:sign-up"))  
        #     return render(request, "main/signup.html", {
        # 'form': form,
        # 'message': 'Form not valid'
        # })
    else:
        form = SignUpForm()


    return render(request, 'main/sign-up.html', {"form": form})



def signIn(request):



    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password= password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("notes:index"))
        else:
            return render(request, "main/sign-in.html", {
                'message': "Invalid credientials"
            })
    
    return render(request, "main/sign-in.html")



def signOut(request):
    user = request.user

    logout(request)
    
    return HttpResponseRedirect(reverse("notes:index"))