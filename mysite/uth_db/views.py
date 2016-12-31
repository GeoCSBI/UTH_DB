from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic 
from .models import Menu

def index(request):
	
	menu_items = Menu.objects.all()
	html = ''	
	for item in menu_items:
		url = '/uth_db/' + str(item.id) + '/'
		html+= '<a href="'+ url + '">'+ item.foodName +'</a><br>'
	return HttpResponse(html)

def detail(request, menu_id):

	return HttpResponse("<h2>Details for id: " + str(menu_id) + "</h2>")
	
	
