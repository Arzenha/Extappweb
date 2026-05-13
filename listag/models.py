from datetime import date
from django.db import models

class RDO(models.Model):
    obra = models.CharField(
        verbose_name='Obra',
        max_length=100,
        null=False,
        blank=False
    )
    responsavel = models.CharField(
        verbose_name='Responsável',
        max_length=100,
        null=False,
        blank=False
    )
    descricao = models.TextField(
        verbose_name='Descrição',
        null=False,
        blank=False
    )
    data = models.DateField(
        verbose_name='Data',
        null=False,
        blank=False
    )
    clima = models.CharField(
        verbose_name='Clima',
        max_length=50,
        null=False,
        blank=False,
        choices=[
            ('ensolarado', 'Ensolarado'),
            ('nublado', 'Nublado'),
            ('chuvoso', 'Chuvoso'),
            ('parcialmente_nublado', 'Parcialmente Nublado'),
            ('tempestuoso', 'Tempestuoso'),
        ]
    )
    funcionarios = models.IntegerField(
        verbose_name='Número de Funcionários',
        null=False,
        blank=False
    )
    observacoes = models.TextField(
        verbose_name='Observações',
        blank=True,
        null=True
    )
    foto = models.ImageField(
        verbose_name='Foto',
        upload_to='rdo_fotos/',
        blank=True,
        null=True
    )
    criado_em = models.DateTimeField(
        verbose_name='Criado em',
        auto_now_add=True
    )
    atualizado_em = models.DateTimeField(
        verbose_name='Atualizado em',
        auto_now=True
    )

    class Meta:
        ordering = ['-data']
        verbose_name = 'RDO'
        verbose_name_plural = 'RDOs'

    def __str__(self):
        return f"{self.obra} - {self.data}"
