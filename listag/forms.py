from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column
from .models import RDO


class RDOForm(forms.ModelForm):
    class Meta:
        model = RDO
        fields = ['obra', 'responsavel', 'descricao', 'data', 'clima', 'funcionarios', 'observacoes', 'foto']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
            'data': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-8'
        self.helper.layout = Layout(
            Row(
                Column('obra', css_class='col-md-6'),
                Column('responsavel', css_class='col-md-6'),
            ),
            Row(
                Column('data', css_class='col-md-4'),
                Column('clima', css_class='col-md-4'),
                Column('funcionarios', css_class='col-md-4'),
            ),
            'descricao',
            'observacoes',
            'foto',
            Submit('submit', 'Salvar RDO', css_class='btn btn-primary mt-3')
        )
