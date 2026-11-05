from django.urls import path, re_path
from .views.dev import DesignView

urlpatterns = [
    re_path(r'^dev/(?P<subpath>.*)$', DesignView.as_view(), name='dev')
]