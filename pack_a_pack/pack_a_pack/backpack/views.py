from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User 
from .models import Trip, Backpack, Profile, Item
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignupForm
# Create your views here.

def signout(request):
	logout(request)
	return HttpResponseRedirect('/')

def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			u = form.cleaned_data['username']
			p = form.cleaned_data['password']
			e = form.cleaned_data['email']
			user = User.objects.create_user(e,p,u)
		return HttpResponse('HI')
	else:
		form = SignupForm()
		return render(request, 'signup.html', {'form': form})

def index(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			u = form.cleaned_data['username']
			p = form.cleaned_data['password']
			user = authenticate(username = u, password = p)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/trips')
				else:
					print('Account disabled / deleted')
			else:
				print('Invalid Credentials')
	else:
		form = LoginForm()
		return render(request, 'index.html', {'form': form})

def trips(request):
	this_user = Profile.objects.get(user=request.user)
	trips = Trip.objects.filter(profile=this_user)

	
	print(trips)
	return render(request, 'trips.html', {'trips': trips})

def trip(request, trip_id):
	return render(request, 'trip.html', {'trip': trip_id})

def backpacks(request):
	return render(request, 'backpacks.html')

 #  	{% for trip in trips %}
	# 	<p>Trip name: {{ trip.name }}</p>
	# 	<p>Location: {{trip.location}}</p>
	# 	<p>Backpacks: {{trip.backpacks}}</p>
	# 	<p>Notes: {{trip.notes}}</p>
	# 	<hr />
	# {% endfor %}
