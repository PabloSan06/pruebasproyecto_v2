from django import forms
from datetime import date
from django.forms import ValidationError

def solo_caracteres(value):
    if any(char.isdigit() for char in value ):
        raise ValidationError('Solo letras por favor. %(valor)s',
                            code='Error1',
                            params={'valor':value})
        #raise ValidationError('El nombre no puede contener números.')


class ContactoForm(forms.Form):

    SEGMENTO_MERCADO = (
        ('','-Seleccione una opción-'),
        (1,'Industria'),
        (2,'Comercio'),
        (3,'Producción'),
    )

    nombre = forms.CharField(
            label='Razon social',
            required=False,
            validators=(solo_caracteres,),
            widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese solo texto'})
            )
    email = forms.EmailField(
            label='Email',
            max_length=50,
            error_messages={
                    'required': 'Por favor completa el campo',                    
                },
            widget= forms.TextInput(attrs={'class':'form-control','type':'email'})
            )
    asunto = forms.CharField(
            label='Asunto',
            max_length=100,
            widget= forms.TextInput(attrs={'class':'form-control'})
        )
    mensaje = forms.CharField(
            label='Observaciones ',
            max_length=500,
            widget=forms.Textarea(attrs={'class':'form-control','rows':5}))


    segmento_mercado = forms.ChoiceField(
        label='Segmento de mercado',
        choices=SEGMENTO_MERCADO,
        initial='2',
        widget=forms.Select(attrs={'class':'form-control'})
    )
    
    def clean_mensaje(self):
        data = self.cleaned_data['mensaje']
        if len(data) < 10:
            raise ValidationError("Debes especificar mejor el mensaje que nos envias")
        return data
    
    def clean(self):
        cleaned_data = super().clean()
        asunto = cleaned_data.get("asunto")
        

        if  asunto  not in asunto:
            msg = "Debe decir las copas de boca."
            self.add_error('asunto', msg)

