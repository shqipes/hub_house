from django.db import models
from django.urls import reverse

# Create your models here.
""" tabella anagrafica raccoglie i dati generali del rapporto"""


""" queste tabelle definiscono i confini 
    e le varie zona dove si effettuano i lavori"""



""" queste tabelle definiscono il rapporto di lavoro"""

class Mese(models.Model):
    anno = models.IntegerField()
    mese = models.CharField(max_length=9)
    fotobusta = models.ImageField(blank=True, null=True)
    pagabusta = models.IntegerField(blank=True, null=True)
    oremese = models.IntegerField(blank=True, null=True)
    differenza_ore = models.IntegerField()
    saldato = models.BooleanField(blank=True, default=False,)
    
    def __str__(self):
        return self.mese
    
    class Meta:
        verbose_name = 'Mese'
        verbose_name_plural = 'Mesi'  
        
    def get_all_orari(self):
        return Orario.objects.filter(mese_appartenenza=self).order_by("data")
    
    def get_number_giorni_in_mese(self):
        return Orario.objects.filter(mese_appartenenza=self).count()
    
    

class Orario(models.Model):
    data = models.CharField(max_length=10, blank=True, null=True)
    ore = models.IntegerField()
    mese_appartenenza = models.ForeignKey(Mese, on_delete=models.CASCADE, related_name="orari", blank=True, null=True)
    
    class Meta:
        verbose_name = "Orario"
        verbose_name_plural = "Orari"
        
    def __str__(self):
        return self.data
    
    def get_absolute_url(self):
        return reverse("visualizza_orario", kwargs={"pk": self.pk})
    
    def get_all_attivita(self):
        return Azione.objects.filter(lavoro_appartenenza=self).order_by("nome_azione")

        

class Intervento(models.Model):
    nome_int = models.CharField(max_length=20)
    descrizione_intervento = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = "Intervento"
        verbose_name_plural = "Interventi"
        
    def __str__(self):
        return self.nome_int


        
class Azione(models.Model):
    nome_azione = models.CharField(max_length=20)
    descrizione_azione = models.CharField(max_length=200)
    tempo_azione = models.IntegerField()
    intervento_appartenenza = models.ManyToManyField(Intervento)
    lavoro_appartenenza = models.ForeignKey(Orario, on_delete=models.CASCADE, related_name="Azioni")
    
    class Meta:
        verbose_name = "Azione"
        verbose_name_plural = "Azioni"
        
    def __str__(self):
        return self.nome_azione
    
    def get_absolute_url(self):
        return reverse("lista_attivita", kwargs={"pk": self.pk})


        
        
        
""" le tabelle di sopra definiscono il rapporto di lavoro"""
