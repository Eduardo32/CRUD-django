from django import forms
from controleClientes.models import Cliente


class InsereClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente

        fields = [
            'nome',
            'sobrenome',
            'telefone',
            'email',
        ]
