from django import forms
from .models import Azione, Orario, Intervento


class FormOreLavoro(forms.ModelForm):
    class Meta:
        model = Orario
        fields = ["data", "ore"]
        
        
class FormAttivitalavoro(forms.ModelForm):
    class Meta:
        model = Azione
        fields = ["nome_azione", "descrizione_azione", "tempo_azione"]
        

        
       