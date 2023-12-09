from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse


# Create your views here.
def HomeView(request):
	return render(request, "core/homepage.html")
