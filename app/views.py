from django.shortcuts import render

# Create your views here.

def userfilters(request):
    d={'data':'Hey There HOw arE you'}
    return render(request,'userfilters.html',d)