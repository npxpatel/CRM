from django.urls import path
from .views import AgentsListView, AgentCreateView, AgentDetailView, AgentUpdateView, AgentDeleteView

app_name= 'agents'

urlpatterns = [
     path('', AgentsListView.as_view(), name='agent-list'),
     path('create/', AgentCreateView.as_view(), name='agent-create'),
     path('<int:pk>/', AgentDetailView.as_view(), name='agent-detail'),
     path('update/<int:pk>/', AgentUpdateView.as_view(), name='agent-update'),
     path('delete/<int:pk>/', AgentDeleteView.as_view(), name='agent-delete'), 
]