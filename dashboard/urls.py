from django.conf.urls import url

from . import views


app_name = 'dashboard'
urlpatterns = [
    url(r'^dashboardbase$', views.dashboardbase, name="dashboardbase"),
    url(r'^getValueFromForm$', views.getValueFromForm, name='getValueFromForm'),
    url(r'^testForm$', views.testForm, name='testForm'),
    url(r'^testFormResult$', views.testFormResult, name='testFormResult'),
    
    url(r'^stationDetails/([0-9]+)$', views.stationDetails, name='stationDetails'),
    
    url(r'^loginPage$', views.loginPage, name='loginPage'),
    url(r'^login$', views.login, name='name'),
    url(r'^$', views.dashboard, name='dashboard'),
    
    url(r'^showFlows$', views.showFlows, name='showFlows'),
    url(r'^viewPDFOnline$', views.viewPDFOnline, name='viewPDFOnline'),
    
    url(r'^baiduMap$', views.baiduMap, name='baiduMap'),
    
    url(r'^contractInfo$', views.contractInfo, name='contractInfo')
]



