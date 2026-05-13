from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from listag.views import (
    DashboardView,
    RDOListView,
    RDOCreateView,
    RDOUpdateView,
    RDODeleteView,
    RDODetailView,
    RDOPdfView,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DashboardView.as_view(), name='dashboard'),
    path('rdo/', RDOListView.as_view(), name='rdo-lista'),
    path('rdo/criar/', RDOCreateView.as_view(), name='rdo-criar'),
    path('rdo/<int:pk>/', RDODetailView.as_view(), name='rdo-detalhes'),
    path('rdo/<int:pk>/editar/', RDOUpdateView.as_view(), name='rdo-editar'),
    path('rdo/<int:pk>/deletar/', RDODeleteView.as_view(), name='rdo-deletar'),
    path('rdo/<int:pk>/pdf/', RDOPdfView.as_view(), name='rdo-pdf'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
