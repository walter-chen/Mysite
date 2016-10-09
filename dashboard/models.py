from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_unicode


class Station(models.Model):
    station_code = models.CharField(max_length=200, unique=True, blank=False)
    station_name = models.CharField(max_length=300, blank=False)
    district = models.CharField(max_length=50)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=False)
    address = models.CharField(max_length=300)
    def __unicode__(self):
        return smart_unicode(self.station_name)


class Resource(models.Model):
    station_code =  models.ForeignKey(Station, to_field='station_code', on_delete=models.CASCADE)
    resource_name = models.CharField(max_length=300, blank=False)
    resource_code = models.CharField(max_length=300, blank=False)
    def __unicode__(self):
        return smart_unicode(self.resource_name)

class Property(models.Model):
    station_code =  models.ForeignKey(Station, to_field='station_code', on_delete=models.CASCADE)
    contract_code = models.CharField(max_length=200, blank=False)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    contract_type = models.CharField(max_length=200)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)

class Order(models.Model):
    station_code =  models.ForeignKey(Station, to_field='station_code', on_delete=models.CASCADE)
    order_code = models.CharField(max_length=50, blank=False)
    maintenance_id = models.CharField(max_length=50, blank=False)
    alarm_details = models.CharField(max_length=300, blank=False)
    def __unicode__(self):
        return smart_unicode(self.alarm_details)

    
    
    
    
    
    
    