from django.conf.urls import url, include
from . import views

app_name = 'uth_db'

urlpatterns = [
	
	#/uth_db/
	url(r'^$', views.IndexView.as_view(), name="index"),
	

	#uth_db/tables/
	url(r'^tables/$', views.TablesView.as_view(), name='emptyTables'),
	
	]