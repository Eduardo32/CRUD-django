from django.db import models


class Cliente (models.Model):

    nome = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )

    sobrenome = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )

    telefone = models.CharField(
        max_length=16,
        null=True,
        blank=True
    )

    email = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    def __str__(self):
        return "%s %s" % (self.nome, self.sobrenome)

    objetos = models.Manager()
