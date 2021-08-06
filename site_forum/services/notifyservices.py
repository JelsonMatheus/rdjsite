from notifications.signals import notify

def notify_answer(request, topico, resposta):
    recipient = resposta.parent.user if resposta.parent else topico.user
    verb = 'responder'
    description = f'{recipient} respondeu seu post em {topico.titulo}.'
    url = topico.get_absolute_url() + f'#post{resposta.pk}'

    if request.user.pk != recipient.pk:
        notify.send(sender=request.user, recipient=recipient, target=topico, 
               action_object=resposta, verb=verb, description=description, url=url)