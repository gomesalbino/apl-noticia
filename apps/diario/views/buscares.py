from django.shortcuts import   render
from diario.models import Noticia


def buscar(request):
    """Faz a busca por noticiarios"""
    lista_noticias = Noticia.objects.order_by('-data_noticia').filter(publicada=True)
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET["buscar"]
        if buscar:
            lista_noticias = lista_noticias.filter(titulo_noticia__icontains=nome_a_buscar)
    
    dados = {
        'noticias' : lista_noticias
    }
    return render(request, "noticia/buscar.html", dados)