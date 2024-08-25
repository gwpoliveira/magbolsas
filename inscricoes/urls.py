from django.urls import path
from django.contrib.auth import views as auth_views
from .views import inscricao_view, inscricao_sucesso, download_excel, lista_inscritos

urlpatterns = [
    path('', inscricao_view, name='inscricao'),  # Página inicial de inscrição
    path('sucesso/', inscricao_sucesso, name='inscricao_sucesso'),  # Página de sucesso após inscrição
    path('download_excel/', download_excel, name='download_excel'),  # Rota para download do Excel
    path('lista_inscritos/', lista_inscritos, name='lista_inscritos'),  # Rota para listar inscritos
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Página de login
    path('logout/', auth_views.LogoutView.as_view(next_page=''), name='logout'),  # Rota para logout
]
