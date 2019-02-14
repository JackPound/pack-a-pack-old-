from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User 
from .models import Trip, Backpack, Profile, Item, Packed
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
			user = User.objects.create_user(u,e,p)
			user = authenticate(username = u, password = p)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/')
				else:
					print('Account disabled / deleted')
			else:
				print('Invalid Credentials')
			return HttpResponseRedirect('/')
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
					return HttpResponseRedirect('/')
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
	profile = Profile.objects.get(user = request.user)
	trip = Trip.objects.get(id = trip_id)
	packs = Backpack.objects.filter(trip = trip_id)
	print('profile',profile.user.username)
	print(request.user.id)
	try:
		unused_packs = Backpack.objects.filter(profile = profile).exclude(trip = trip_id)
	except:
		unused_packs = []
	return render(request, 'trip.html', {'trip': trip, 'packs': packs, 'unused_packs': unused_packs})

def backpacks(request):
	form = BackpackForm()
	p = Profile.objects.get(user=request.user)
	packs = Backpack.objects.filter(profile = p)
	return render(request, 'backpacks.html', {'packs': packs, 'form': form})

def backpack(request, pack_id):
	pack = Backpack.objects.get(id = pack_id)
	packed_items = Packed.objects.order_by('item__name').filter(backpack = pack)
	all_items = Item.objects.order_by('name').all()
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
	backpack = Backpack.objects.get(id=pack_id)
	item = Item.objects.get(id=item_id)
	try:
		Packed.objects.get(backpack=backpack, item=item)
		existing_item = Packed.objects.get(backpack=pack_id, item=item_id)
		existing_item.count += 1
		existing_item.save()
		print(existing_item.count)
	except:
		Packed.objects.create(backpack=backpack, item=item, count=1)
	url = '/backpacks/'+str(pack_id)
	return HttpResponseRedirect(url)

def unpack_item(request, pack_id, each_id):
	packed = Packed.objects.get(id=each_id)
	packed.count -= 1
	if packed.count == 0:
		packed.delete()
	else:
		packed.save()
	print(packed.item)
	print(packed.backpack)
	url = '/backpacks/'+str(pack_id)
	return HttpResponseRedirect(url)


