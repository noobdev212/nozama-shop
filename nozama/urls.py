from django.urls import path, re_path
from .views import DesignView, TestView

urlpatterns = [
    re_path(r'^dev/(?P<subpath>.*)$', DesignView.as_view(), name='dev'),
    path('test/', TestView.as_view(), name='test-template')
]