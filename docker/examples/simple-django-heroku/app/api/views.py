from django.shortcuts import render
from django.views import View
from django.http import JsonResponse



# Create your views here.
class ApiHomeView(View):

    def get(self, request):
        welcome_message = 'Welcome to the API'
        json_response = {
            'message': welcome_message,
            'status': 200,
        }
        return JsonResponse(json_response)
