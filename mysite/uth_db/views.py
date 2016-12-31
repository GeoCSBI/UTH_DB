from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic 
from .models import Menu

def index(request):
	
	menu_items = Menu.objects.all()
	context = {
		'menu_items':menu_items,
	}
	return render(request, 'uth_db/index.html', context)

def detail(request, menu_id):

	try:
		menu_item = Menu.objects.get(pk=menu_id)
	except Menu.DoesNotExist:
		raise Http404("Directory Not Found!")

	return render(request, 'uth_db/details.html', {'menu_item':menu_item})

	
	
