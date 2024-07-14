"""
URL configuration for metrogen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from metrogenapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.CommonHome, name='CommonHome'),
    path('Gallery',views.Gallery, name='Gallery'),
    path('Home',views.Home, name='Home'),
    path('TransportationSignUp', views.TransportationSignUp, name='TransportationSignUp'),
    path('AboutUs', views.About_Us, name='About Us'),
    path('chk',views.lgdata, name='chk'),
    path('Lg_chk',views.lgdata, name='chk'),
    path('SignUp', views.Customer_Registration, name='SignUp'),

    path('AdminHome', views.AdminHome, name='Admin Home'),
    path('AdminViewCustomers', views.AdminViewCustomers, name='Admin View Customers'),
    path('AdminAddEmployee', views.AdminAddEmployee, name='AdminAddEmployee'),

    path('AdminAddStay', views.AdminAddStay, name='Admin Add Stay'),
    path('AdminAddStations', views.AdminAddStations, name='Admin Add Station'),
    path('AdminAddTiming', views.AdminAddTiming, name='Admin Add Timing'),
    path('AdminAddFair', views.AdminAddFair, name='Admin Add Fair'),

    path('AdminViewFeedback', views.AdminViewFeedback, name='AdminViewFeedback'),
    path('AdminViewJob', views.AdminViewJob, name='AdminViewJob'),
    path('AdminViewTransportation', views.AdminViewTransportation, name='AdminViewTransportation'),
    path('AdminViewJobApplications', views.AdminViewJobApplications, name='AdminViewJobApplications'),
    path('AdminViewTransporterJobApplications', views.AdminViewTransporterJobApplications, name='AdminViewTransporterJobApplications'),
    path('CustomerUpdateTime',views.CustomerViewTiming),

    path('EmployeeAddFair', views.EmployeeAddFair, name='Employee Add Fair'),
    path('EmployeeAddStations', views.EmployeeAddStations, name='Employee Add Station'),
    path('EmployeeAddTiming', views.EmployeeAddTiming, name='Employee Add Timing'),
    path('EmployeeHome', views.EmployeeHome, name='Employee Home'),
    path('EmployeeAddJob', views.EmployeeAddJob, name='Employee Add Job'),
    path('EmployeeViewTicketBooking', views.EmployeeViewTicket, name='Employee Ticket'),
    path('EmployeeViewTransportations', views.EmployeeViewTransporation, name='EmployeeViewTransportation'),
    path('EmployeeViewConfirmedBooking', views.EmployeeViewTransporationConfirmed, name='EmployeeViewConfirmedTransportation'),

    path('CustomerHome', views.Customer_Home, name='Customer Home'),
    path('CustomerBookTickets', views.CustomerBookTickets, name='CustomerBookTickets'),
    path('CustomerAddFeedback', views.CustomerAddFeedback),
    path('CustomerViewJob', views.CustomerView, name='CustomerViewJob'),
    path('CustomerUploadResume', views.CustomerUploadResume, name='CustomerUploadResume'),
    path('CustomerSearchStay', views.CustomerSearchStay, name='CustomerSearchStay'),
    path('CustomerSearchTransportation', views.CustomerSearchTransportation, name='CustomerSearchTransportation'),
    path('CustomerBookTransportation', views.CustomerBookTransportation, name='CustomerBookTransportation'),
    path('CustomerViewConfBooking', views.CustomerViewConfimedTransporation, name='CustomerViewConfirmedTransportation'),
    path('CustomerViewTimings',views.CustomerViewTiming),
    path('CustomerBookTransport',views.CustomerBookTransport),
    path('logout',views.logout),


    path('TransportationHome', views.TransportationHome, name='TransportationHome'),
    path('TransportationViewBooking', views.TransportationViewBooking, name='TransportationViewBooking'),
    path('TransportationViewConfirmedBooking', views.TransportationViewConfirmedBooking,
         name='TransportationViewConfirmedBooking'),
    path('CancelBooking',views.CancelBooking),

    path('payment1', views.payment1, name='payment1'),
    path('payment2', views.payment2, name='payment2'),
    path('payment3', views.payment3, name='payment3'),
    path('payment4', views.payment4, name='payment4'),
    path('payment5', views.payment5, name='payment5'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)