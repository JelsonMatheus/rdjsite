from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from .models import Topico, Forum

# Create your views here.

def redirect_to_forum_view(request):
    forum = Forum.objects.all().first()
    return redirect(forum)

@login_required
def logout_view(request):
    logout(request)
    return redirect(request.get_full_path())
    

class TopicoListView(ListView):

    queryset = Topico.objects
    context_object_name = 'topicos'
    template_name = 'site_forum/index.html'
    paginate_by = 10
    ordering = ['updated_at']

    def get_queryset(self):
        self.forum = get_object_or_404(Forum, slug=self.kwargs['slug'])
        return super().get_queryset().filter(forum=self.forum)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['foruns'] = Forum.objects.all()
        context['forum_atual'] = self.forum
        return context