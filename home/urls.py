from django.urls import path
from . import views

app_name = 'user1'

urlpatterns = [
	path('home/', views.HomeView.as_view(), name='home'),
]