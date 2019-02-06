from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import services

from .models import TrainDetails
def format(data, type):
    fields = ['PNR', 'Status', 'TrainDetails', 'Boarding', 'Destination', 'Date', 'CoachType']
    details = {}
    try:
        if type == 'pnr':
            for i in range(len(fields)):
                details[fields[i]] = data[i]
        elif type == 'train':
            details['Source'] = data[0]
            details['Destination'] = data[1]
    except:
        details = {"ERROR":"Unable to retrive details, please check the detail provided "}

    return details

class PnrView(APIView):
    def get(self, request):
        if 'pnrno' in request.GET:
            data = services.getPnrDetails(request.GET['pnrno'])
            print(data)
            data = format(data, 'pnr')
        else:
            data = {"Error":"Send a GET request for a PNR"}
        return Response(data, status=200)

class TrainView(APIView):
    def get(self, request):
        if 'trainno' in request.GET:
            data = services.getTrainDetails(request.GET['trainno'])
            print(data)
            data = format(data, 'train')
        else:
            data = {"Error":"Send a GET request for a TrainNo"}
        return Response(data, status=200)
