from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def feeCollection(request):
    return render(request, 'finance/feeCollection.html')

def feeDuesReport(request):
    return render(request, 'finance/feeduer.html')

def feeCollectionReport(request):
    return render(request, 'finance/feecolr.html')
