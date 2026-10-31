from django.shortcuts import render
from django.views import View

class DesignView(View):
    template_name = "dev/design.html"

    def get(self, request):
        return render(request, self.template_name)