from django.contrib import admin

from dashboard.models import Station, Resource


class ResourceInline(admin.ModelAdmin):
    model = Resource
    extra = 3

class StationAdmin(admin.ModelAdmin):
    fieldsets = (
            (None, {
                'fields':('station_code', 'station_name', 'longitude', 'latitude')
                }),
            ('Advanced options',{
                'classes':('collapse',),
                'fields':('resource_code', 'resource_name'),
            })
        )
    inlines = [ResourceInline]

admin.site.register(Station, StationAdmin)