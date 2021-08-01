from django.http import JsonResponse
from django.views.generic.base import View
from django.core.exceptions import ImproperlyConfigured
from django.http.response import HttpResponseForbidden
from site_forum.models import Resposta, Topico

class FilterMixin:
    filter_fields = []

    def get_queryset_filter(self, request):
        params = request.GET
        filter_dict = {}

        for key in set(params.keys()).intersection(set(self.filter_fields)):
            filter_dict[key] = params[key]
        
        return self.queryset.filter(**filter_dict)

class JSONMixin:
    fields = []
    data_name = 'data'

    def response_to_json(self, context):
        return JsonResponse(context)
    
    def get_data_json(self, queryset):
        data = []        
        for obj in list(queryset.values(*self.fields)):
            data.append(obj)
        
        return data

class JSONModelView(View, JSONMixin, FilterMixin):
    queryset = None

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            context = self.get_context_data(**kwargs)
            return self.response_to_json(context)
        else:
            return HttpResponseForbidden('Autenticação necessária.')
    
    def get_queryset(self, **kwargs):
        if self.queryset is None:
            raise ImproperlyConfigured('JSONModelview requer um queryset atributo.')

        queryset = self.get_queryset_filter(self.request)
        return queryset
    
    def get_context_data(self, **kwargs):
        queryset = self.get_queryset(**kwargs)
        data = self.get_data_json(queryset)
        context = {'count': len(data)}
        context[self.data_name] = data

        return context
    

class JSONTopicoView(JSONModelView):
    queryset = Topico.objects
    filter_fields = ['pk']
    fields = ['titulo', 'texto']

class JSONRespostaView(JSONModelView):
    queryset = Resposta.objects
    filter_fields = ['pk']
    fields = ['texto', 'parent__id']
        


