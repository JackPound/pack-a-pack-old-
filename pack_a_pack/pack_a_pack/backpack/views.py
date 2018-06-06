from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User 
from .models import Trip, Backpack, Profile, Item
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignupForm, TripForm, BackpackForm
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
	if request.method == 'POST':
		form = TripForm(request.POST)
		if form.is_valid():
			na = form.cleaned_data['name']
			l = form.cleaned_data['location']
			no = form.cleaned_data['notes']
			p = Profile.objects.get(user=request.user)
			# print("name:",na,"location:",l,"notes:",no)
			new_trip = Trip.objects.create(name = na, location = l, notes = no, profile = p)
			return HttpResponseRedirect('/trips')
	else:
		this_user = Profile.objects.get(user=request.user)
		trips = Trip.objects.filter(profile=this_user)
		form = TripForm()
		return render(request, 'trips.html', {'trips': trips, 'form': form})

def trip(request, trip_id):
	trip = Trip.objects.get(id = trip_id)
	packs = Backpack.objects.filter(trip = trip_id)
	unused_packs = Backpack.objects.exclude(trip = trip_id)
	return render(request, 'trip.html', {'trip': trip, 'packs': packs, 'unused_packs': unused_packs})

def backpacks(request):
	form = BackpackForm()
	p = Profile.objects.get(user=request.user)
	packs = Backpack.objects.filter(profile = p)
	return render(request, 'backpacks.html', {'packs': packs, 'form': form})

def backpack(request, pack_id):
	pack = Backpack.objects.get(id = pack_id)
	packed_items = Item.objects.filter(backpack = pack_id)
	all_items = Item.objects.all()
	return render(request, 'backpack.html', {'pack': pack, 'packed_items':packed_items, 'all_items': all_items})

def remove_pack(request, pack_id, trip_id):
	trip = Trip.objects.get(id = trip_id)
	trip.backpacks.remove(pack_id)
	url = '/trips/'+str(trip_id)
	return HttpResponseRedirect(url)

def add_pack(request):
	trip = Trip.objects.get(id = request.POST['trip_id'])
	trip.backpacks.add(request.POST['pack_id'])
	trip.save()
	url = '/trips/'+str(request.POST['trip_id'])
	return HttpResponseRedirect(url)

def create_pack(request):
	n = request.POST['name']
	s = request.POST['size']
	p = Profile.objects.get(user=request.user)
	new_pack = Backpack.objects.create(name = n, size = s, profile = p)
	return HttpResponseRedirect('/backpacks')

def delete_pack(request, pack_id):
	Backpack.objects.filter(id=pack_id).delete()
	return HttpResponseRedirect('/backpacks')

def pack_item(request, pack_id, item_id):
	backpack = Backpack.objects.get(id = pack_id)
	backpack.packed_items.add(item_id)
	backpack.save()
	url = '/backpacks/'+str(pack_id)
	return HttpResponseRedirect(url)

def unpack_item(request):
	return HttpResponse('hi')


