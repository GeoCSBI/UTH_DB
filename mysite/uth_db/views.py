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
from django.views.generic import View
from .models import Food, Table
from .forms import UserForm, BookingForm, OrderForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login	
from django.http import HttpResponseRedirect

def noBooking(request):
	return render(request, 'uth_db/tables.html', {})

class IndexView(generic.ListView):

	template_name = 'uth_db/index.html'

	def get_queryset(self):
		return Food.objects.all()

class TablesView(generic.ListView):

	template_name = 'uth_db/tables.html'
	def get_queryset(self):
		return Table.objects.all()

class BookingFormView(View):
	form_class = BookingForm
	template_name = 'uth_db/mybooking_form.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form':form})

	#process form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			booking = form.save(commit=False)
			available = False

			#cleaned (normalized) data
			dateBooked = form.cleaned_data['dateBooked']
			timeBooked = form.cleaned_data['timeBooked']
			booking.bookedBy = User.objects.get(id=request.user.id)
			persons = form.cleaned_data['persons']
			
			tables = Table.objects.all()
			booking.save()

			for table in tables:

				print table.seats

				if (table.isBooked == False) & (table.seats >= persons):
					print 'hello'
					available = True
					table.isBooked = True
					table.booking = booking
					table.save()
					break
			
			if available == False:

				temp = 0
				tempTables = []
				for table in tables:

					if table.isBooked == False:
						
						temp += table.seats
						tempTables.append(table)
						
						if temp >= persons:
							for item in tempTables:
								item.isBooked = True
								item.booking = booking
								item.save()
							break
			if available == False:
				booking.delete()
				return HttpResponseRedirect('/uth_db/not_available')

		else:

			print form.errors

		
		return HttpResponseRedirect('/uth_db/')



class OrderFormView(View):

	form_class = OrderForm
	template_name = 'uth_db/order.html'

	#COOLEST THING ABOUT CLASS BASED VIEW!!
	#handling both GET and POST req through the same URL

	#display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form':form})

	#process form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			order = form.save(commit=False)

			#cleaned (normalized) data
			order.save()

		return render(request, self.template_name, {'form':form})


class UserFormView(View):

	form_class = UserForm
	template_name = 'uth_db/registration_form.html'

	#COOLEST THING ABOUT CLASS BASED VIEW!!
	#handling both GET and POST req through the same URL

	#display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form':form})

	#process form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			#cleaned (normalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			#returns User objects if credential are correct
			user = authenticate(username=username, password=password)

			if user is not None:
				if user.is_active:
					login(request, user) #they are now logged in
					return redirect('uth_db:index')

		return render(request, self.template_name, {'form':form})







