from django.db import models
from django.core.exceptions import ValidationError


class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    data_emprestimo = models.DateTimeField(auto_now_add=True)

    data_devolucao = models.DateTimeField(
        null=True,
        blank=True
    )

    devolvido = models.BooleanField(default=False)

    # 🚫 Impede empréstimo de livro indisponível
    def clean(self):
        if not self.devolvido and not self.livro.disponivel:
            raise ValidationError(
                "Este livro já está emprestado."
            )

    def __str__(self):
        return f"{self.usuario} pegou {self.livro}"