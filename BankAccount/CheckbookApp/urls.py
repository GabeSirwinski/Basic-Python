from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('AddTransaction', views.addTransaction, name="addtransaction"),
    path('BalanceSheet', views.balanceSheet, name="balancesheet"),
    path('CreateNewAccount', views.createNewAccount, name="createnewaccount"),
]
