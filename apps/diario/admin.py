from django.contrib import admin

from .models import Noticia

class ListaNoticias(admin.ModelAdmin):
    list_display = ('id', 'titulo_noticia', 'materias', 'foto_noticia', 'data_noticia', 'publicada')
    list_display_links =('id', 'titulo_noticia')
    search_fields = ('titulo_noticia',)
    list_filter = ('data_noticia',)
    list_editable = ('publicada',)
    list_per_page = 10

admin.site.register(Noticia, ListaNoticias)
