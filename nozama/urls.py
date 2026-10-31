from django.urls import path 
from .views import DesignView

urlpatterns = [
    path('dev/', DesignView.as_view(), name='design')
]