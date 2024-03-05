from django.urls import path
from . import views

urlpatterns = [
    path('feecol/',views.feeCollection),
    path('feeduer/',views.feeDuesReport),
    path('feecolr/',views.feeCollectionReport),
]

