

from django.urls import path
from  .views import noticias, buscares


urlpatterns = [
    path('', noticias.index, name='index'),
    path('<int:noticia_id>', noticias.noticia, name='noticia'),
    path('buscar', buscares.buscar, name="buscar"),
    path('cria_noticia', noticias.cria_noticia, name='cria_noticia'),
    path('deleta/<int:noticia_id>', noticias.deleta_noticia, name='deleta_noticia'),
    path('edita/<int:noticia_id>', noticias.editar_noticia, name='editar_noticia'),
    path('atualiza_noticia', noticias.atualiza_noticia,  name='atualiza_noticia')
]