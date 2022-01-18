from django.urls import path
from api import views
from api.apps import ApiConfig


app_name = ApiConfig.name
urlpatterns = [
    # example: /api/v1/
    path('', views.ApiHomeView.as_view(), name='home')
]
