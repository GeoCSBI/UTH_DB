# from django.shortcuts import render
# from django.http import HttpResponse, Http404
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth import authenticate, login
# from django.views import generic 
# from .models import Food, Table, Booking

# def index(request):
	
# 	menu_items = Food.objects.all()
# 	context = {
# 		'menu_items':menu_items,
# 	}
# 	return render(request, 'uth_db/index.html', context)

# def detail(request, menu_id):

# 	menu = get_object_or_404(Menu, pk=menu_id)
# 	return render(request, 'uth_db/details.html', {'menu':menu})

# def emptyTables(request):
	
# 	empty_tables = Table.objects.all()
# 	context = {
# 		'empty_tables':empty_tables,
# 	}
# 	return render(request, 'uth_db/tables.html', context)

# #TODO: Add userId
# def mybookings(request):

# 	#change all with filter key=userId
# 	mybookings = Booking.objects.all()
# 	mytable = Table.objects.all()
# 	context = {
# 		'mybookings':mybookings,
# 		'mytable':mytable
# 	}
# 	return render(request, 'uth_db/mybookings.html', context)
	

from django.views import generic
from .models import Food, Table

class IndexView(generic.ListView):

	template_name = 'uth_db/index.html'

	def get_queryset(self):
		return Food.objects.all()

class TablesView(generic.ListView):

	template_name = 'uth_db/tables.html'
	def get_queryset(self):
		return Table.objects.all()
