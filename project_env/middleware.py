from django.utils.deprecation import MiddlewareMixin # Support for old MIDDLEWARE_CLASSES and asynchronous request
from django.conf import settings
from django.http import HttpResponseBadRequest
from django.urls import resolve, reverse
from django.shortcuts import redirect

class SandboxMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
        Verify if environment is set to sandbox
        otherwise, return HTTP error 400
        """
        url_path = reverse(resolve(request.path).view_name)
        if url_path.startswith('/dev'):
            if not settings.ENVIRONMENT:
                print(f'Please define environment in settings')
                return HttpResponseBadRequest('Environment is currently set as None')
            elif not settings.ENVIRONMENT.endswith('sandbox'):
                print(f'Environment not configured to sandbox')
                return HttpResponseBadRequest('Request is not available')
        
        response = self.get_response(request)
        return response
