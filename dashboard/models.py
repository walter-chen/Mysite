from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_unicode


class District(models.Model):
    district_name = models.CharField(max_length=50, primary_key=True)

class Client(models.Model):
    client_name = models.CharField(max_length=100, primary_key=True, blank=True)

class Station(models.Model):
    station_code = models.CharField(max_length=200, primary_key=True, blank=False)
    station_name = models.CharField(max_length=300, blank=False)
    district = models.ForeignKey(District, to_field='district_name', on_delete=models.CASCADE)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=False)
    address = models.CharField(max_length=300)
    def __unicode__(self):
        return smart_unicode(self.station_name)


class Resource(models.Model):
    station_code =  models.ForeignKey(Station, to_field='station_code', on_delete=models.CASCADE)
    district = models.ForeignKey(District, to_field='district_name', on_delete=models.CASCADE)
    resource_code = models.CharField(max_length=200, primary_key=True,blank=False)
    resource_name = models.CharField(max_length=300, blank=False)
    def __unicode__(self):
        return smart_unicode(self.resource_name)

class Property(models.Model):
    station_code =  models.ForeignKey(Station, to_field='station_code', on_delete=models.CASCADE)
    contract_code = models.CharField(max_length=200, blank=False, primary_key=True)
    district = models.ForeignKey(District, to_field='district_name', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    price_per_year = models.DecimalField(max_digits=9, decimal_places=2, blank=False)
    contract_type = models.CharField(max_length=200)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)

class Order(models.Model):
    station_code =  models.ForeignKey(Station, to_field='station_code', on_delete=models.CASCADE)
    order_code = models.CharField(max_length=50, primary_key=True, blank=False)
    maintenance_id = models.CharField(max_length=50, blank=False)
    alarm_details = models.CharField(max_length=300, blank=False)
    def __unicode__(self):
        return smart_unicode(self.alarm_details)

class Project(models.Model):
    station_code = models.ForeignKey(Station, to_field='station_code', on_delete=models.CASCADE)
    project_code = models.CharField(max_length=50, primary_key=True, blank=False)
    district = models.ForeignKey(District, to_field='district_name', on_delete=models.CASCADE)
    construction_type = models.CharField(max_length=200, blank=False)
    tower_type = models.CharField(max_length=200, blank=True)
    room_type = models.CharField(max_length=200, blank=True)
    investment_price = models.DecimalField(max_digits=10, decimal_places=2)
    
class Indent(models.Model):
    station_code = models.ForeignKey(Station, to_field='station_code', on_delete=models.CASCADE)
    indent_code = models.CharField(max_length=50, primary_key=True, blank=False)
    district = models.ForeignKey(District, to_field='district_name', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    indent_status = models.CharField(max_length=100, blank=False)
    client = models.ForeignKey(Client, to_field='client_name', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    
class AssetSource(models.Model):
    source = models.CharField(max_length=50, primary_key=True)
    
    def __unicode__(self):
        return smart_unicode(self.source)
    def __str__(self):
        return self.source

class CoverageScene(models.Model):
    type = models.CharField(max_length=100, primary_key=True)
    
    def __unicode__(self):
        return smart_unicode(self.type)
    def __str__(self):
        return self.type

class StationAccounting(models.Model):
    station_code = models.ForeignKey(Station, to_field='station_code', on_delete=models.CASCADE)
    station_name = models.CharField(max_length=255, blank=False)
    fetch_data_date = models.DateField(blank=False)  #last day of month
    district = models.ForeignKey(District, to_field='district_name', on_delete=models.CASCADE)
    source = models.ForeignKey(AssetSource, to_field='source', on_delete=models.CASCADE)
    tower_type = models.CharField(max_length=300)
    coverage_scene = models.ForeignKey(CoverageScene, to_field='type', on_delete=models.CASCADE)
    profit_rate = models.DecimalField(max_digits=10, decimal_places=2)
    profit = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        unique_together = ('station_name', 'fetch_data_date')  
      
    def __unicode__(self):  
        return '%s,%d'%(self.station_name,self.fetch_data_date)
    
    
    
    
    
    
    