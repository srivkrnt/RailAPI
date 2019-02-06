from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import TrainDetails
class TrainView(APIView):
    def get(self, request):
        return Response({"result":200}, status=200)
