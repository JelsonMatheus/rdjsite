from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class ForumPageView(TemplateView):

    template_name = 'core_site/index.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)