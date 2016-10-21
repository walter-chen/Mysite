# -*- coding: utf-8 -*-
import time

from django.db.models.aggregates import Count, Max, Sum
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from reportlab.pdfgen import canvas

from dashboard.models import Station, Order, Resource, Property, Indent, Project, \
    District, Client
from dashboard.utilies import TowerCounter


def dashboard(request):
    stationInfos = District.objects.annotate(num_stations=Count('station'))
    contractInfos = District.objects.annotate(num_contracts=Count('property'))
    investmentAmount = District.objects.annotate(investment=Sum('project__investment_price'))
    indentIncomes = District.objects.annotate(incomes=Sum('indent__price'))
    propertyPrice = District.objects.annotate(price=Sum('property__price'))
    simiClientOfferMoney = Client.objects.annotate(money=Sum('indent__price')) \
                .filter(indent__district_id="思明区")
    
    context = {"stationInfos":stationInfos,
               "contractInfos":contractInfos,
               "investmentAmount":investmentAmount,
               "indentIncomes":indentIncomes,
               "propertyPrice":propertyPrice,
                "simClientOfferMoney":simiClientOfferMoney}
    return render(request, 'dashboard/dashboard.html', context)
def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    return HttpResponseRedirect("/dashboard/testForm")
def loginPage(request):
    return render(request, 'dashboard/loginPage.html', {})


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

def showFlows(request):
    
    return render(request, "dashboard/dashboard-flow.html", {})

def viewPDFOnline(request):
    with open('/home/cc/Documents/关于加强站址规范交维管控的通知正文.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
    pdf.closed

def baiduMap(request):
    return render(request, "dashboard/baiduMap.html",{})

def contractInfo(request):
    ISOTIMEFORMAT='%Y'
    YEAR = time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )
    DISTRICT_LIST = ['思明区','海沧区','湖里区','翔安区','集美区','同安区']
    MONTH_BEGIN_LIST = ['01-01','02-01','03-01','04-01','05-01','06-01','07-01','08-01','09-01','10-01','11-01','12-01']
    MONTH_END_LIST = ['01-31','02-28','03-31','04-30','05-31','06-30','07-31','08-31','09-30','10-31','11-30','12-31']
    columnData = [[],[],[],[],[],[]]
    
    for i in [0,1,2,3,4,5]:
        for j in [0,1,2,3,4,5,6,7,8,9,10,11]:
            columnData[i].append(Property.objects.filter(district_id=DISTRICT_LIST[i], end_date__gte=YEAR+"-"+MONTH_BEGIN_LIST[j], end_date__lte=YEAR+"-"+MONTH_END_LIST[j]).count())
    propertys = Property.objects.filter(end_date__gte=YEAR+"-01-01", end_date__lte=YEAR+"-12-31")
    
    context = {
               'DISTRICT_LIST':DISTRICT_LIST,
               'columnData':columnData,
               'propertys':propertys
               }
        
    return render(request, "dashboard/contractInfo.html", context)
    




