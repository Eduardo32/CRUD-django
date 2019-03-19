from django.views.generic import TemplateView, CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from controleClientes.models import Cliente
from website.forms import InsereClienteForm
from django.urls import reverse_lazy


class IndexTemplateView(TemplateView):
    template_name = 'website/index.html'


class ClienteListView(ListView):
    template_name = 'website/listar.html'
    model = Cliente
    context_object_name = 'Clientes'


class ClienteDetailView(DetailView):
    template_name = 'website/detalhes.html'
    model = Cliente
    context_object_name = 'Cliente'


class ClienteUpdateView(UpdateView):
    template_name = 'website/editar.html'
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('website:clientes')


class ClienteCreateView(CreateView):
    template_name = 'website/salvar.html'
    model = Cliente
    form_class = InsereClienteForm
    success_url = reverse_lazy('website:clientes')


class ClienteDeleteView(DeleteView):
    model = Cliente
    context_object_name = 'cliente'
    success_url = reverse_lazy('website:clientes')

