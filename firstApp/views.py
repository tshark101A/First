from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

Names ={"Tushar": "This is Tushar's space!", "Vikas":"This is Vikas' space!", "Dippu":"Ye Dippu ka thela hai!"}

def Responder(request, name):
    try:
        curName = Names[name]
        return HttpResponse(curName)
    except:
        return HttpResponseNotFound("404: No one I know with that name !")
    
def Responder2(request, name):
   try:
    keyName = list(Names.keys())
    curName = keyName[name-1]
    redirectPath = reverse("stringArg", args=[curName])
    return HttpResponseRedirect(redirectPath)
   except:
        return HttpResponseNotFound("404: No one I know with that name !")

