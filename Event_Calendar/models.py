from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.exceptions import ValidationError
import datetime

# Create your models here.
class Event(models.Model):
	event_title = models.CharField(max_length=200)
	description = models.TextField()
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	created_by=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

	def save(self, *args, **kwargs):
		if self.end_time < self.start_time:
			raise ValidationError("The date cannot be in the past!")
		else:
			super(Event, self).save(*args, **kwargs)

	def __str__(self):
		return self.event_title

	@property
	def get_html_url(self):
		url = reverse('event_edit', kwargs={'event_id':self.pk})
		return f'<a href="{url}"> {self.event_title} </a>'