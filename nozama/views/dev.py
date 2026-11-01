from django.shortcuts import render
from django.views import View
from django.template.loader import render_to_string
from django.urls import resolve
import logging 

logger = logging.getLogger('main')

# use this view for working with test.html
# this would not be pushed to production but
# rather, this is a tool to view designs
class DesignView(View):
    template_name = 'dev/design.html'

    def get(self, request, subpath):
        logger.info(__class__)
        context = {}
        # verify if there exist trailing path from /dev/
        if subpath: 
            logger.debug(f'extracted {subpath}')
            view_class = resolve(f'/{subpath}/').func.view_class
            context['content'] = render_to_string(view_class.template_name)
            logger.info(context['content'])

        return render(request, self.template_name, context)