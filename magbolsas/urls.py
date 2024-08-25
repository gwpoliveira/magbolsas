from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para o admin padrão do Django
    path('inscricao/', include('inscricoes.urls')),  # Inclui as rotas do app `inscricoes`
    path('', RedirectView.as_view(url='/inscricao/', permanent=True)),  # Redireciona a raiz para `/inscricao/`
]
