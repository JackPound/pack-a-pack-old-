from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Item(models.Model):
	name = models.CharField(max_length=100)
	size = models.IntegerField()
	category = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Backpack(models.Model):
	name = models.CharField(max_length=100)
	size = models.IntegerField()
	items = models.ManyToManyField(Item, blank=True)
	def __str__(self):
		return self.name

class Trip(models.Model):
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	notes = models.CharField(max_length=300)
	backpacks = models.ManyToManyField(Backpack, blank=True)
	def __str__(self):
		return self.name
	
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	backpacks = models.ForeignKey(Backpack, blank=True, null=True, on_delete=models.CASCADE)
	trips = models.ForeignKey(Trip, blank=True, null=True, on_delete=models.CASCADE)
	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()
