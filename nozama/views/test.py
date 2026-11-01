from django.views import View
from django.shortcuts import render
import logging

logger = logging.getLogger('main')

class TestView(View):
    template_name = 'test/test.html'

    def get(self, request):
        logger.info(__class__)
        return render(request, self.template_name)