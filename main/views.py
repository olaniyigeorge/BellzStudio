from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
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

@login_required(login_url='/sign-in')
def updateProfile(request):
    user = request.user
    if not user.is_authenticated:
        user = None
        return render(request, 'main/my-profile.html', {"user": user})
    
    if request.method == "POST":
        print(request.POST)
        user = User.objects.get(id=user.id)
        print(user)
        if len(request.POST["first_name"]) > 0:
            user.first_name = str(request.POST["first_name"])
            print(request.POST["first_name"])
            user.save()
        if len(request.POST["last_name"]) > 0:
            user.last_name = str(request.POST["last_name"])
            print(request.POST["last_name"])
            user.save()
        user = User.objects.get(id=user.id)

        update = False
        return HttpResponseRedirect(reverse("main:profile"))
        #return render(request, 'main/my-profile.html', {"user": user, "update": update})
    
    update = True
    return render(request, 'main/my-profile.html', {"user": user, "update": update})


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
        reader = request.POST['reader'] or "off"
        print("Email:", email)
        print("Password:", password)
        print("Reader:", reader)


        if password != password_confirmation:
            print()
            return HttpResponseRedirect(reverse("main:sign-up"))    
        
        try:
            user, created = User.objects.get_or_create(email=email, password=password)
            print("User: ", user, created)
    
            #save user
            
            user.save()
            if reader == 'on':
                reader = Reader.objects.get_or_create(user=user)
                

        except Exception as e:
            print("Error during creation: ", e)
            return HttpResponseRedirect(reverse("main:sign-up"))
                
        try:

            # Get username and password for authentication
            email = request.POST['email']
            raw_password = request.POST['password']

            # Log user in with username and raw password
            print("User before auth: ", user)
            # user = authenticate(request, email=email, password=raw_password)
            
            if user:
                print("logging in...")
                login(request, user)
                print("Logged in")
                return HttpResponseRedirect(reverse("notes:index"))
        
            print("Couldn't log authencate user: ", user)
            return HttpResponseRedirect(reverse("main:index"))     
        except Exception as e:
            print("Error during auth/login: ", e)
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
        print("Email:", email)
        print("Password:", password)
        print("User before auth:", request.user)
        user = authenticate(request, email=email, password=password)
        print("User after auth:", user)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("notes:index"))
        else:
            print("User: ", user)
            return render(request, "main/sign-in.html", {
                'error': f"Error-{user}"
            })
    
    return render(request, "main/sign-in.html")

def signOut(request):
    user = request.user

    logout(request)
    
    return HttpResponseRedirect(reverse("notes:index"))