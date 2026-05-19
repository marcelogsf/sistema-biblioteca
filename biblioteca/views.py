import csv

from django.http import HttpResponse
from django.shortcuts import render

from .models import Emprestimo, Livro, Usuario


# 📊 EXPORTAR CSV
def exportar_emprestimos_csv(request):

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

    writer.writerow([
        'Livro',
        'Usuário',
        'Data do Empréstimo',
        'Data da Devolução',
        'Status'
    ])

    emprestimos = Emprestimo.objects.select_related(
        'livro',
        'usuario'
    ).all()

    for e in emprestimos:

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


# 📊 RELATÓRIO
def relatorio_emprestimos(request):

    emprestimos = Emprestimo.objects.all()

    livro_id = request.GET.get('livro')
    usuario_id = request.GET.get('usuario')
    devolvido = request.GET.get('devolvido')

    if livro_id:
        emprestimos = emprestimos.filter(
            livro_id=livro_id
        )

    if usuario_id:
        emprestimos = emprestimos.filter(
            usuario_id=usuario_id
        )

    if devolvido in ['true', 'false']:
        emprestimos = emprestimos.filter(
            devolvido=(devolvido == 'true')
        )

    return render(request, "admin/relatorio.html", {
        "emprestimos": emprestimos,
        "livros": Livro.objects.all(),
        "usuarios": Usuario.objects.all(),

        "total_emprestimos": Emprestimo.objects.count(),
        "devolvidos": Emprestimo.objects.filter(
            devolvido=True
        ).count(),

        "pendentes": Emprestimo.objects.filter(
            devolvido=False
        ).count(),
    })