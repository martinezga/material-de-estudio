
from django.http.response import JsonResponse
from django.views import View


class MainView(View):
    def get(self, request):
        response = {
            "Status": "up and running"
        }

        return JsonResponse(response)
