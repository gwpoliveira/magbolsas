from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inscricao/', include('inscricoes.urls')),  # Rota para as inscrições
    path('', RedirectView.as_view(url='/inscricao/', permanent=True)),  # Redireciona a raiz para /inscricao/
]
