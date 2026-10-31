from django.shortcuts import render
from django.views import View
from django.template.loader import render_to_string
from django.urls import resolve

# use this view for working with test.html
# this would not be pushed to production but
# rather, this is a tool to view designs
class DesignView(View):
    template_name = 'dev/design.html'

    def get(self, request, subpath):
        context = {}
        # verify if there exist trailing path from /dev/
        if subpath: 
            view_class = resolve(f'/{subpath}/').func.view_class
            context['content'] = render_to_string(view_class.template_name)

        return render(request, self.template_name, context)

class TestView(View):
    template_name = 'test/test.html'

    def get(self, request):
        return render(request, self.template_name)