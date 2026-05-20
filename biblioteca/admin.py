from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.urls import path
from django.shortcuts import redirect
import csv

from .models import Livro, Usuario, Emprestimo


# 📊 EXPORTAR CSV
def exportar_csv(modeladmin, request, queryset):
    response = HttpResponse(
        content_type='text/csv; charset=utf-8'
    )

    response['Content-Disposition'] = (
        'attachment; filename="relatorio_emprestimos.csv"'
    )

    # ✅ Corrige acentos no Excel
    response.write('\ufeff')

    writer = csv.writer(
        response,
        delimiter=';'
    )

    # 📌 Cabeçalhos
    writer.writerow([
        'Livro',
        'Usuário',
        'Data do Empréstimo',
        'Data da Devolução',
        'Status'
    ])

    # 📌 Dados
    for e in queryset:

        data_emprestimo = (
            e.data_emprestimo.strftime('%d/%m/%Y às %H:%M')
            if e.data_emprestimo else '-'
        )

        data_devolucao = (
            e.data_devolucao.strftime('%d/%m/%Y às %H:%M')
            if e.data_devolucao else '-'
        )

        status = (
            '✅ Devolvido'
            if e.devolvido
            else '❌ Pendente'
        )

        writer.writerow([
            e.livro.titulo,
            e.usuario.nome,
            data_emprestimo,
            data_devolucao,
            status
        ])

    return response


exportar_csv.short_description = "Exportar empréstimos para CSV"


# 📚 ADMIN DE LIVROS
class LivroAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'autor',
        'status_disponibilidade'
    )

    search_fields = (
        'titulo',
        'autor'
    )

    # 🔎 FILTRO LATERAL
    list_filter = (
        'disponivel',
    )

    def status_disponibilidade(self, obj):
        if obj.disponivel:
            return "✅ Disponível"

        return "❌ Emprestado"

    status_disponibilidade.short_description = "Status"


# 👤 ADMIN DE USUÁRIOS
class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'email',
        'possui_emprestimos'
    )

    search_fields = (
        'nome',
        'email'
    )

    # 🔎 FILTRO LATERAL
    list_filter = (
        'emprestimo__devolvido',
    )

    def possui_emprestimos(self, obj):

        if obj.emprestimo_set.exists():
            return "📚 Já pegou livro"

        return "❌ Nunca pegou"

    possui_emprestimos.short_description = "Empréstimos"


# 📚 ADMIN DE EMPRÉSTIMOS
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = (
        'livro',
        'usuario',
        'data_emprestimo',
        'data_devolucao',
        'devolvido'
    )

    actions = [exportar_csv]

    search_fields = (
        'livro__titulo',
        'usuario__nome'
    )

    list_filter = (
        'devolvido',
        'data_emprestimo'
    )

    def save_model(self, request, obj, form, change):
        from django.utils import timezone

        if obj.devolvido and obj.data_devolucao is None:
            obj.data_devolucao = timezone.now()

        super().save_model(
            request,
            obj,
            form,
            change
        )


# 🎨 ADMIN CUSTOMIZADO
class BibliotecaAdmin(admin.AdminSite):
    site_header = "Sistema Biblioteca"
    site_title = "Biblioteca"
    index_title = "Painel Administrativo"

    def get_urls(self):
        urls = super().get_urls()

        custom_urls = [
            path(
                'relatorio/',
                self.admin_view(
                    self.relatorio_view
                )
            )
        ]

        return custom_urls + urls

    def relatorio_view(self, request):
        return redirect('/relatorio/')


# 🚀 INSTÂNCIA DO ADMIN
admin_site = BibliotecaAdmin(
    name='biblioteca_admin'
)


# 📌 REGISTROS
admin_site.register(Livro, LivroAdmin)
admin_site.register(Usuario, UsuarioAdmin)
admin_site.register(Emprestimo, EmprestimoAdmin)

# 🔐 AUTENTICAÇÃO
admin_site.register(User)
admin_site.register(Group)