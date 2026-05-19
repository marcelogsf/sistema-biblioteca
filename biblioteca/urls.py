from django.urls import path
from . import views

urlpatterns = [
    path('exportar-csv/', views.exportar_emprestimos_csv, name='exportar_csv'),
    path('relatorio/', views.relatorio_emprestimos, name='relatorio'),
]