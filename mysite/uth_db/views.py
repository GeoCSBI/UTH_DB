from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views import generic 
from .models import Food

def index(request):
	
	menu_items = Food.objects.all()
	context = {
		'menu_items':menu_items,
	}
	return render(request, 'uth_db/index.html', context)

def detail(request, menu_id):

	
	menu = get_object_or_404(Menu, pk=menu_id)
	return render(request, 'uth_db/details.html', {'menu':menu})

	
	
