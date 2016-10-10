# -*- coding: utf-8 -*-
from django.db.models.aggregates import Count, Max, Sum
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response

from dashboard.models import Station, Order, Resource, Property, Indent, Project, \
    District


def dashboard(request):
    stationInfos = District.objects.annotate(num_stations=Count('station'))
    contractInfos = District.objects.annotate(num_contracts=Count('property'))
    investmentAmount = District.objects.annotate(investment=Sum('project__investment_price'))
    indentIncomes = District.objects.annotate(incomes=Sum('indent__price'))
    propertyPrice = District.objects.annotate(price=Sum('property__price'))
    context = {"stationInfos":stationInfos,
               "contractInfos":contractInfos,
               "investmentAmount":investmentAmount,
               "indentIncomes":indentIncomes,
               "propertyPrice":propertyPrice}
    return render(request, 'dashboard/dashboard.html', context)
def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    return HttpResponse(username + "fsdf"+ password)
def loginPage(request):
    return render(request, 'dashboard/signin.html', [])


def testForm(request):
    return render(request, 'dashboard/dashboard-search.html', {})
def testFormResult(request):
    keyword = request.GET.get('keyword', '')
    stations = list(Station.objects.filter(station_name__contains=keyword))
    return render(request, 'dashboard/dashboard-search.html', {'stations':stations})
def stationDetails(request, station_code):
    station = Station.objects.get(station_code = station_code)
    highTemperatureAmount = list(Order.objects.filter(station_code=station_code, alarm_details__contains="温度")).__len__()
    powerFailureAmount = list(Order.objects.filter(station_code=station_code, alarm_details__contains="停电")).__len__()
    waterLoggingAmount = list(Order.objects.filter(station_code=station_code, alarm_details__contains="水浸")).__len__()
    batteryAmount = list(Order.objects.filter(station_code=station_code, alarm_details__contains="电池")).__len__()
    
    alarmAmount = sum([highTemperatureAmount, 
                      powerFailureAmount, 
                      waterLoggingAmount,
                      batteryAmount])
   
    resourcesList = list(Resource.objects.filter(station_code = station_code))
    contractsList = list(Property.objects.filter(station_code = station_code))
    indentsList = list(Indent.objects.filter(station_code = station_code))
    projectsList = list(Project.objects.filter(station_code = station_code))
    
    if alarmAmount!=0:
        highTemperatureRatio = float(highTemperatureAmount)/alarmAmount
        
        powerFailureRatio = float(powerFailureAmount)/alarmAmount
        waterLoggingRatio = float(waterLoggingAmount)/alarmAmount
        batteryRatio = float(batteryAmount)/alarmAmount
        othersRatio = 1-powerFailureRatio-waterLoggingRatio-batteryRatio
        
        context = {'station':station,
                   'resources':resourcesList,
                   'contracts':contractsList,
                   'indents':indentsList,
                   'projects':projectsList,
                   'highTemperatureRatio':highTemperatureRatio,
                   'powerFailureRatio':powerFailureRatio,
                   'waterLoggingRatio':waterLoggingRatio,
                   'batteryRatio':batteryRatio,
                   'othersRatio':othersRatio}
    else:
        context={'station':station,
                 'resources':resourcesList,
                 'contracts':contractsList,
                 'indents':indentsList,
                 'projects':projectsList} 
                   
    return render(request, 'dashboard/station-details.html', context)





def getValueFromForm(request):
    provider = request.POST.get('checkboxes1', '')
    provider += request.POST.get('checkboxes2', '')
    provider += request.POST.get('checkboxes3', '')
    return HttpResponse(provider)

def dashboardbase(request):
    station = Station.objects.get(pk=1)
    return render(request, "dashboard/dashboard-base.html", {'station': station})










