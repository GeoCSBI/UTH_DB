from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

app_name = 'uth_db'

urlpatterns = [
	
	#/uth_db/
	url(r'^$', views.IndexView.as_view(), name="index"),
	
	#Login/Logout url
	url(r'^login/$', auth_views.login, {'template_name' : 'uth_db/login.html'}, name='login'),
	url(r'^logout/$', auth_views.logout, {'template_name' : 'uth_db/logout.html'}, name='logout'),

	#uth_db/tables/
	url(r'^tables/$', views.TablesView.as_view(), name='emptyTables'),

	url(r'^register/$', views.UserFormView.as_view(), name="register"),
	
	url(r'^booking/$', views.BookingFormView.as_view(), name="booking"),

	url(r'^not_available/$', views.noBooking, name="failed"),

	url(r'^order/$', views.OrderFormView.as_view(), name="order")
	
	]