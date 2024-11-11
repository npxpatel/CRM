from typing import Any
import random
from django.db.models.query import QuerySet
from django.shortcuts import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganiserAndLoginRequiredMixin
from django.core.mail import send_mail

# Create your views here.

class AgentsListView(OrganiserAndLoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
    
    context_object_name = 'agents'

class AgentCreateView(OrganiserAndLoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organiser = False 
        user.set_password(f"{random.randint(0, 1000)}")
        user.save()
        Agent.objects.create(user=user, organisation=self.request.user.userprofile)     
        send_mail(
            subject= "Invitation for being our Agent",
            message="Visit site to reset your password as a confirmation step",
            from_email="np21@gmail.com",
            recipient_list=[user.email]
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('agents:agent-list')
    
class AgentDetailView(OrganiserAndLoginRequiredMixin, generic.DetailView):
    template_name = 'agents/agent_detail.html'
    context_object_name = 'agent'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

    def get_success_url(self):
        return reverse('agents:agent-list')


class AgentUpdateView(OrganiserAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/agent_update.html'
    form_class = AgentModelForm

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
    
    def get_success_url(self):
        return reverse('agents:agent-list')       
    

class AgentDeleteView(OrganiserAndLoginRequiredMixin, generic.DeleteView):
    template_name  = 'agents/agent_delete.html'
    queryset = Agent.objects.all()

    def get_success_url(self):
        return reverse('agents:agent-list')    
    
    


