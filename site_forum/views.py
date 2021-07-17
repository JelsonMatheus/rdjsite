from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.base import View
from django.views.generic.edit import FormView
from .models import Resposta, Topico, Forum
from .forms import UserRegisterForm, UserLoginForm, TopicoCreateForm

# Create your views here.

def redirect_to_forum_view(request):
    forum = Forum.objects.all().first()
    return redirect(forum)

@login_required
def logout_view(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER','/'))
    

class LoginView(FormView):
    template_name = 'site_forum/registration/login.html'
    form_class = UserLoginForm

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form):
        messages.error(self.request, form.non_field_errors()[0])
        return HttpResponseRedirect(self.request.path)
    
    def get_success_url(self):
        return self.request.GET.get('next', '/')

class RegisterView(FormView):
    template_name = 'site_forum/registration/register.html'
    success_url = '/'
    form_class = UserRegisterForm
    initial = {'username':''}

    def form_valid(self, form):
        login(request=self.request, user=form.save())
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.error(self.request, "Erro ao registrar o usuário!")
        return super().form_invalid(form)
        
class TopicoListView(ListView):

    queryset = Topico.objects
    context_object_name = 'topicos'
    template_name = 'site_forum/index.html'
    paginate_by = 15
    ordering = ['updated_at']

    def get_queryset(self):
        self.forum = get_object_or_404(Forum, slug=self.kwargs['slug'])
        return super().get_queryset().filter(forum=self.forum)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TopicoCreateForm
        context['foruns'] = Forum.objects.all()
        context['forum_atual'] = self.forum
        return context

class TopicoCreateView(View):

    def post(self, request, *args, **kwargs):
        form = TopicoCreateForm(request.POST)
        user = request.user
        forum = Forum.objects.get(slug=kwargs['slug'])

        if form.is_valid():
            topico = form.save(user, forum)
            return redirect(topico)
        else:
            return redirect(forum)


class RepostaListView(ListView):
    queryset = Resposta.objects.filter(deleted_at__isnull=True)
    get_context_data = 'respostas'
    template_name = 'site_forum/topico.html'
    paginate_by = 15
    ordering = ['created_at']

    def get_queryset(self):
        self.topico = get_object_or_404(Topico, pk=self.kwargs['topico_id'])
        return super().get_queryset().filter(topico=self.topico)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forum_atual'] = get_object_or_404(Forum, slug=self.kwargs['slug'])
        context['foruns'] = Forum.objects.all()
        context['topico'] = self.topico
        return context
