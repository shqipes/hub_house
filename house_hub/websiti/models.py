from django.db import models

# Create your models here.

class Tipologia(models.Model):
	nome = models.CharField(max_length=20)
 
class Categoria(models.Model):
    settore = models.CharField(max_length=20)

# class Sito(models.Model):
# 	titolo = 
# 	urlsito =
# 	nomeutente =
# 	pwutente =
# 	conto_carta =
# 	contenuto = 
# 	immagine =
# 	tipologia =
# 	categoria =


    