
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView,CreateView
from .models import Conversation, Message, Notification
from django.shortcuts import redirect 
from django.urls import reverse_lazy


class ConversationCreateView(LoginRequiredMixin, CreateView):
    model = Conversation
    fields = []  # Pas de champ visible, on ajoute juste le participant courant
    template_name = 'messaging/conversation_create.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.participants.add(self.request.user)
        return response

    def get_success_url(self):
        return reverse_lazy('messaging:detail', kwargs={'pk': self.object.pk})


class ConversationListView(LoginRequiredMixin, ListView):
    template_name = 'messaging/conversations.html'
    context_object_name = 'conversations'

    def get_queryset(self):
        return Conversation.objects.filter(participants=self.request.user)

class ConversationDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        conversation = get_object_or_404(Conversation, pk=pk)
        if request.user not in conversation.participants.all():
            return redirect('messaging:list')  # Sécurité : l'utilisateur n'est pas dans cette conversation
        return render(request, 'messaging/conversation_detail.html', {
            'conversation': conversation
        })

    def post(self, request, pk):
        conversation = get_object_or_404(Conversation, pk=pk)
        content = request.POST.get('content')
        if content:
            Message.objects.create(
                conversation=conversation,
                sender=request.user,
                content=content
            )
        return redirect('messaging:detail', pk=pk)

class NotificationListView(LoginRequiredMixin, ListView):
    template_name = 'messaging/notifications.html'
    context_object_name = 'notifications'

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)
