from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Lead, Agent
from django.views import generic
from .froms import LeadModelForm


#CBV :

class LandingPageView(generic.TemplateView):
     template_name = 'landing.html' 
  


class LeadListView(generic.ListView):
      template_name = 'leads/lead_list.html'
      queryset = Lead.objects.all()
      context_object_name = 'leads'


class LeadDetailView(generic.DetailView):
    template_name = 'leads/lead_details.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'


class LeadCreateView(generic.CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm

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
