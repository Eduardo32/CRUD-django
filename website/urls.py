from django.urls import path
from website.views import IndexTemplateView, ClienteListView, ClienteDetailView, ClienteUpdateView, ClienteCreateView, ClienteDeleteView


app_name = 'website'

urlpatterns = [
    path('',
         IndexTemplateView.as_view(),
         name='index'
         ),

    path('clientes/',
         ClienteListView.as_view(),
         name='clientes'
         ),

    path('cliente/<pk>/',
         ClienteDetailView.as_view(),
         name='detalhes'
         ),

    path('cliente/editar/<int:pk>/',
         ClienteUpdateView.as_view(),
         name='editar'
         ),

    path('cliente/salvar/',
         ClienteCreateView.as_view(),
         name='salvar'
         ),

    path('cliente/excliur/<pk>',
         ClienteDeleteView.as_view(),
         name='excluir'
         )
]
