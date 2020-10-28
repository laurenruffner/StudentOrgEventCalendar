from django.db import models

# Create your models here.

class Organization(models.Model):
    org_name = models.CharField(max_length = 200)
    org_url = models.CharField(max_length = 200)
    org_description = models.CharField(max_length = 200)
    org_category = models.CharField(max_length = 200)

class Event(models.Model):
    organizaiton = models.ForeignKey(Organization, on_delete=models.CASCADE)
    event_name = models.CharField(max_length = 200)
    event_datetime = models.DateTimeField('Start date and time of event')
    event_description = models.CharField(max_length = 200)
