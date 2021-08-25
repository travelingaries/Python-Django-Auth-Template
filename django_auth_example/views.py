from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')
