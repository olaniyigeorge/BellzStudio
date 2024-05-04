from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.



def index(request):
    
    return render(request, 'main/index.html', {})


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
            'icon_link': 'images/my-twitter.png'               
        },
        "linkedin": {
            'link': 'https://linkedin.com/abeleje-olaniyi',
            'username': 'Abeleje Olaniyi',
            'icon_link': 'images/my-linkedin.png'               
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