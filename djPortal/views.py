from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

def landingPage(request):
    return render(request, 'index.html')