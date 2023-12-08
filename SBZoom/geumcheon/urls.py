from django.urls import path

from . import views

appname = 'geumcheon'

urlpatterns = [
    path("", views.index, name="index"),
    path("eatOut", views.eatOut, name="eatOut"),
    path("service", views.service, name="service"),
    path("retail", views.retail, name="retail"),
    path("total", views.total, name="total"),
    path("ilban", views.ilban, name="ilban"),
    path("franchise", views.franchise, name="franchise"),
    path("totalStores", views.totalStores, name="totalStores"),
    path("totalSales", views.totalSales, name="totalSales"),
]