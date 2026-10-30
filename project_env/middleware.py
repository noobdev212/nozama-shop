from django.utils.deprecation import MiddlewareMixin # Support for old MIDDLEWARE_CLASSES and asynchronous request
from django.conf import Settings
from django.http import HttpResponseBadRequest

class SandboxMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
        Verify if environment is set to sandbox
        otherwise, return HTTP error 400
        """
        if not Settings.ENVIRONMENT:
            print(f'Please define environment in settings')
            return HttpResponseBadRequest('Environment is currently set as None')
        elif not Settings.ENVIRONMENT.endswith('sandbox'):
            print(f'Environment not configured to sandbox')
            return HttpResponseBadRequest('Request is not available')
        
        response = self.get_response(request)
        return response
