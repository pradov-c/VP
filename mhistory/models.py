from django.db import models
from django.utils import timezone

class Patient(models.Model):
	name = models.CharField(max_length=60)
	ci = models.CharField(max_length=15,primary_key=True)
	register_date = models.DateTimeField(default=timezone.now)	
	
	def register(self):
		self.register_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name

