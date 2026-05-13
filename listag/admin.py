from django.contrib import admin
from .models import RDO

@admin.register(RDO)
class RDOAdmin(admin.ModelAdmin):
    list_display = ('obra', 'responsavel', 'data', 'clima', 'funcionarios')
    list_filter = ('data', 'clima')
    search_fields = ('obra', 'responsavel')
    date_hierarchy = 'data'
    readonly_fields = ('criado_em', 'atualizado_em')

