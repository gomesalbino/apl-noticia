from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Noticia(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo_noticia = models.CharField(max_length=100)
    materias = models.TextField()
    foto_noticia = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    data_noticia = models.DateTimeField(default=datetime.now, blank=True)
    publicada = models.BooleanField(default=False)


    def __str__(self):
        return self.titulo_noticia


