from django.urls import path
from .views import inscricao_view, inscricao_sucesso

urlpatterns = [
    path('', inscricao_view, name='inscricao'),
    path('sucesso/', inscricao_sucesso, name='inscricao_sucesso'),
]
