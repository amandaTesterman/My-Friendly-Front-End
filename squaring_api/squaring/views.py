from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.

class SquaringView(View):
    def get(self, request, number):
        return HttpResponse(number ** 2)

class RoarLouderView(View):
    def get(self, request):
        return HttpResponse("Roar Louder")