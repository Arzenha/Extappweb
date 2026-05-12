from django.contrib import admin
from django.urls import path

from listag.views import (
    EscolaView,
    EscolaCreateView,
    EscolaUpdateView,
    EscolaDeleteView,
    EscolaCompleteView,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', EscolaView.as_view(), name='escola-lista'),
    path('escola/criar/', EscolaCreateView.as_view(), name='escola-criar'),
    path('escola/<int:pk>/editar/', EscolaUpdateView.as_view(), name='escola-editar'),
    path('escola/<int:pk>/deletar/', EscolaDeleteView.as_view(), name='escola-deletar'),
    path('escola/<int:pk>/finalizar/', EscolaCompleteView.as_view(), name='escola-finalizar'),
]
