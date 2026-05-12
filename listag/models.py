from datetime import date
from django.db import models

class Escola(models.Model):
        titulo = models.CharField(
                verbose_name='Título',
                max_length=100, 
                null=False, 
                blank=False
                )
        data_criacao = models.DateTimeField(
                auto_now_add=True, 
                null=False, 
                blank=False
                )
        data_entrega = models.DateTimeField(
                null=False, 
                blank=False
                )
        data_finalizada = models.DateTimeField(null=True)
        
        class Meta:
                ordering = ['data_criacao']
        
        def mark_as_completed(self):
                self.data_finalizada = date.today()
                self.save()