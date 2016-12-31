from django.conf.urls import url, include
from . import views

app_name = 'uth_db'

urlpatterns = [
	
	#/uth_db/
	url(r'^$', views.index, name="index"),
	
	#/uth_db/id/
	url(r'^(?P<menu_id>[0-9]+)/$', views.detail, name="detail"),

	#uth_db/tables/
	url(r'^tables/$', views.emptyTables, name='empyTables'),
	
	#uth_db/tables/
	url(r'^mybookings/$', views.mybookings, name='mybookings')
	]