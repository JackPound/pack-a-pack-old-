from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

class Item(models.Model):
	name = models.CharField(max_length=100)
	size = models.IntegerField()
	category = models.CharField(max_length=100)
	def __str__(self):
		return self.name

	
class Backpack(models.Model):
	name = models.CharField(max_length=100)
	size = models.IntegerField()
	packed_items = models.ManyToManyField(Item, through='Packed', blank=True)
	profile = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.CASCADE)
	def __str__(self):
		return self.name
	def current_volume(self):
		volume = 0
		stuff = Packed.objects.filter(backpack = self)
		for each in stuff:
			volume += each.item.size * each.count
		return volume
	def remaining_volume(self):
		return (self.size - self.current_volume())

class Trip(models.Model):
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	notes = models.CharField(max_length=300)
	backpacks = models.ManyToManyField(Backpack, blank=True)
	profile = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.CASCADE)
	def __str__(self):
		return self.name

class Packed(models.Model):
	backpack = models.ForeignKey(Backpack, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	count = models.IntegerField(null=True)

