from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import User
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