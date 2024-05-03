from django.shortcuts import render
import datetime 
import time
# Create your views here.





def index(request):
    
    d = datetime.datetime.now()
    t = time.time()
    return render(request, 'notes/index.html', {"d": d, 't': t})