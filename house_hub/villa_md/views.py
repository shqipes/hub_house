#from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView

#from .forms import DiscussioneModelForm, PostModelForm
#from .mixins import StaffMixing
from .models import Azione, Mese, Orario, Intervento
from .forms import FormOreLavoro, FormAttivitalavoro

class HomeVilla(ListView):
    queryset = Mese.objects.all()
    template_name = "villa_md/lista_mesi.html"
    context_object_name = "lista_mesi"

class CreaMese(CreateView):
    model = Mese
    fields = "__all__"
    template_name = "villa_md/crea_mese.html"
    success_url = "/"
    
def visualizza_mese(request, pk):
    mese = get_object_or_404(Mese, pk=pk)
    lavoro_mese = Orario.objects.filter(mese_appartenenza=mese)
    context = {"mese": mese, "lavorogiorni": lavoro_mese}
    return render(request, "villa_md/singolo_mese.html", context)

def crea_orelavoro(request, pk):
    mese = get_object_or_404(Mese, pk=pk)
    if request.method == "POST":
        form = FormOreLavoro(request.POST)
        if form.is_valid():
            orario = form.save(commit=False)
            orario.mese_appartenenza = mese
            orario.save()
            return HttpResponseRedirect(orario.get_absolute_url())
    else:
        form = FormOreLavoro()
    context = {"form": form, "mese":mese,}
    return render(request, "villa_md/crea_gg_lavoro.html", context)

def visualizza_orario(request, pk):
    orario = get_object_or_404(Orario, pk=pk)
    azioni_orario = Azione.objects.filter(lavoro_appartenenza=orario)
    context = {"orario": orario, "azioni_orario": azioni_orario}
    return render(request, "villa_md/singolo_orario.html", context)

def aggiungi_attivita(request, pk):
    orario = get_object_or_404(Orario, pk=pk)
    if request.method == "POST":
        form = FormAttivitalavoro(request.POST)
        if form.is_valid():
            azione = form.save(commit=False)
            azione.lavoro_appartenenza = orario
            azione.save()
            return HttpResponseRedirect(azione.get_absolute_url())
    else:
        form = FormAttivitalavoro()
        context = {"form": form, "orario": orario}
        return render(request, "villa_md/aggiungi_attivita.html", context)

def visualizza_attivita(request, pk):
    azione = get_object_or_404(Azione, pk=pk)
    context = {"azione": azione}
    return render(request, "villa_md/lista_attivita.html", context)

class CreaIntervento(CreateView):
    model = Intervento
    fields = "__all__"
    template_name = "villa_md/crea_intervento.html"
    success_url = "villa_md/lista_interventi.html"
    
class ListaInterventi(ListView):    
    queryset = Intervento.objects.all
    template_name = "villa_md/lista_interventi.html"
    context_object_name = "lista_interventi"
    