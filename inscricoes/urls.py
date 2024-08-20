from django.urls import path
from .views import inscricao_view

urlpatterns = [
    path('', inscricao_view, name='inscricao'),  # Usa a view que renderiza 'home.html'
]
