from django import forms
from .models import Mantencion

class MantencionForm(forms.ModelForm):
    class Meta:
        model = Mantencion
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'dueño': forms.TextInput(attrs={'class': 'form-control'}),
            'patente': forms.TextInput(attrs={'class': 'form-control'}),
            'kilometraje': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
