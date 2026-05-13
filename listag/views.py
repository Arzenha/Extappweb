from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Sum, Count
from datetime import datetime, timedelta

from .models import RDO
from .forms import RDOForm


class DashboardView(View):
    def get(self, request):
        total_rdos = RDO.objects.count()
        total_funcionarios = RDO.objects.aggregate(Sum('funcionarios'))['funcionarios__sum'] or 0
        rdos_semana = RDO.objects.filter(
            data__gte=datetime.now() - timedelta(days=7)
        ).count()
        
        context = {
            'total_rdos': total_rdos,
            'total_funcionarios': total_funcionarios,
            'rdos_semana': rdos_semana,
        }
        return render(request, 'listag/dashboard.html', context)


class RDOListView(ListView):
    model = RDO
    template_name = 'listag/rdo_lista.html'
    context_object_name = 'rdo_list'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_rdos'] = RDO.objects.count()
        return context


class RDODetailView(DetailView):
    model = RDO
    template_name = 'listag/rdo_detail.html'
    context_object_name = 'rdo'


class RDOCreateView(CreateView):
    model = RDO
    form_class = RDOForm
    template_name = 'listag/rdo_form.html'
    success_url = reverse_lazy('rdo-lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Criar novo RDO'
        return context


class RDOUpdateView(UpdateView):
    model = RDO
    form_class = RDOForm
    template_name = 'listag/rdo_form.html'
    success_url = reverse_lazy('rdo-lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar RDO'
        return context


class RDODeleteView(DeleteView):
    model = RDO
    template_name = 'listag/rdo_confirm_delete.html'
    context_object_name = 'rdo'
    success_url = reverse_lazy('rdo-lista')


class RDOPdfView(View):
    def get(self, request, pk):
        rdo = get_object_or_404(RDO, pk=pk)
        
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
        from reportlab.lib import colors
        from io import BytesIO
        
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)
        
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#1f5496'),
            spaceAfter=30,
            alignment=1
        )
        
        story = []
        
        story.append(Paragraph("RELATÓRIO DIÁRIO DE OBRA (RDO)", title_style))
        story.append(Spacer(1, 0.3*inch))
        
        data = [
            ['Campo', 'Informação'],
            ['Obra', rdo.obra],
            ['Responsável', rdo.responsavel],
            ['Data', rdo.data.strftime('%d/%m/%Y')],
            ['Clima', rdo.get_clima_display()],
            ['Funcionários', str(rdo.funcionarios)],
        ]
        
        table = Table(data, colWidths=[2*inch, 4*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#1f5496')),
            ('TEXTCOLOR', (0, 0), (0, -1), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (0, -1), 11),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        story.append(table)
        story.append(Spacer(1, 0.3*inch))
        
        story.append(Paragraph("<b>Descrição:</b>", styles['Heading3']))
        story.append(Paragraph(rdo.descricao, styles['Normal']))
        story.append(Spacer(1, 0.2*inch))
        
        if rdo.observacoes:
            story.append(Paragraph("<b>Observações:</b>", styles['Heading3']))
            story.append(Paragraph(rdo.observacoes, styles['Normal']))
        
        doc.build(story)
        
        buffer.seek(0)
        response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="RDO_{rdo.obra}_{rdo.data}.pdf"'
        return response

