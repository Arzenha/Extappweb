from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect

from .models import Escola

class EscolaView(ListView):
    model = Escola
    template_name = 'listag/listag_lista.html'
    context_object_name = 'escola_list'


class EscolaCreateView(CreateView):
    model = Escola
    fields = ['titulo', 'data_entrega']
    template_name = 'listag/lista_form.html'
    context_object_name = 'escola'
    success_url = reverse_lazy('escola-lista')

class EscolaUpdateView(UpdateView):
    model = Escola
    fields = ['titulo', 'data_entrega']
    template_name = 'listag/lista_form.html'
    context_object_name = 'escola'
    success_url = reverse_lazy('escola-lista')

class EscolaDeleteView(DeleteView):
    model = Escola
    template_name = 'listag/lista_confirm_delete.html'
    context_object_name = 'escola'
    success_url = reverse_lazy('escola-lista')

class EscolaCompleteView(View):
    def get(self, request, pk):
        escola = get_object_or_404(Escola, pk=pk)
        escola.mark_as_completed()
        return redirect('escola-lista')
