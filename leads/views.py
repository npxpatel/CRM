from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Lead, Agent, User
from django.views import generic
from .froms import LeadModelForm, CustomUserCreationForm


#CBV :

class LandingPageView(generic.TemplateView):
     template_name = 'landing.html' 
  

class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')


class LeadListView(generic.ListView):
      template_name = 'leads/lead_list.html'
      queryset = Lead.objects.all()
      context_object_name = 'leads'


class LeadDetailView(generic.DetailView):
    template_name = 'leads/lead_details.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'


class LeadCreateView(generic.CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm 

    def form_valid(self, form):
        send_mail(
            subject= "Lead Created",
            message="Visit site to view the leads",
            from_email="np21@gmail.com",
            recipient_list=['np22@gmail.com']
        )
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('leads:lead-list') 



class LeadUpdateView(generic.UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead-list')


class LeadDeleteView(generic.DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead-list')



#FBV :

def landing_page(request):
    return render(request, 'landing.html')


def lead_list(request):
    leads = Lead.objects.all()
    context = { 'leads' : leads}
    return render(request, "leads/lead_list.html", context)


def lead_detials(request, pk):
    lead = Lead.objects.get(id = pk)
    context = {'lead' : lead}
    return render(request, 'leads/lead_details.html', context)


def lead_create(request):
    form = LeadModelForm()

    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('/leads')
    
    context = {'form': form}
    return render(request, 'leads/lead_create.html', context)


def lead_update(request, pk):
    lead = Lead.objects.get(id = pk)
    form = LeadModelForm(instance=lead)
        
    if request.method == 'POST':
        form = LeadModelForm(request.POST ,instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/leads')
        
    context = {
        'form' : form,
        'lead' : lead,
        }
    return render(request, 'leads/lead_update.html', context)


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads')


# def lead_create(request):
#     form = LeadForm()

#     if request.method == 'POST':
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             data = { 
#                 'first_name': form.cleaned_data['first_name'],
#                 'last_name': form.cleaned_data['last_name'],
#                 'age': form.cleaned_data['age'],
#                 'agent': Agent.objects.first()
#             }
#             Lead.objects.create(**data)  
#             return redirect('/leads')
    
#     context = {'form': form}
#     return render(request, 'leads/lead_create.html', context)
