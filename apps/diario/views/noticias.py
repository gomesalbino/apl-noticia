from django.shortcuts import  redirect, render, get_object_or_404
from diario.models import Noticia
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib import  messages


def index(request):
    """Pagina principal, renderiza as noticas"""
    noticias = Noticia.objects.order_by('-data_noticia').filter(publicada=True)
    paginator = Paginator(noticias, 6)
    page = request.GET.get('page')
    noticias_por_pagina = paginator.get_page(page)

    dados = {
        'noticias' : noticias_por_pagina
    }

    return render(request, 'index.html', dados)

def noticia(request, noticia_id):
    """Pagina para ver os detalhes das noticias"""
    noticia = get_object_or_404(Noticia, pk=noticia_id)

    noticia_a_exibir = {
        'noticia' : noticia
    }
    return render(request, 'jornalismo/noticia.html', noticia_a_exibir)


def cria_noticia(request):
    """Cria noticia"""
    if request.method == "POST":
        titulo_noticia = request.POST["titulo_noticia"]
        materias = request.POST["materias"]
        foto_noticia = request.FILES["foto_noticia"]
        if not titulo_noticia.strip():
            messages.error(request, "Campo titulo não pode ficar em branco!")
            return redirect('cria_noticia')
        if not materias.strip():
            messages.error(request,"Campo materia não pode ficar em branco!")
            return redirect('cria_noticia') 

        
        user = get_object_or_404(User, pk=request.user.id)
        noticia = Noticia.objects.create(pessoa=user, titulo_noticia=titulo_noticia, materias=materias, foto_noticia=foto_noticia)
        noticia.save()
        messages.success(request,"Noticia criado com sucesso!")
        return redirect('dashboard')
    else:
        return render(request, 'jornalismo/cria_noticia.html')




def deleta_noticia(request, noticia_id):
    """Deleta a noticia"""
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    noticia.delete()
    messages.success(request,"Noticia criado com sucesso!")
    return redirect('dashboard')

def editar_noticia(request, noticia_id):
    """Edita a noticia"""
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    noticia_a_eidtar = {
        'noticia' : noticia
    }
   
    return render(request, 'jornalismo/editar_noticia.html', noticia_a_eidtar)

def atualiza_noticia(request):
    """Apois editar a noticia ai atualiza"""
    if request.method == "POST":
        noticia_id = request.POST["noticia_id"]
        r = Noticia.objects.get(pk=noticia_id)
        r.titulo_noticia = request.POST["titulo_noticia"]
        r.materias = request.POST["materias"]
        if 'foto_noticia' in request.FILES:
            r.foto_noticia = request.FILES["foto_noticia"]
        r.save()
        messages.success(request,"Noticia atualizado com sucesso!")
        return redirect('dashboard')

def campo_vazio(campo):
    """Atalho para não deixar campo vazio"""
    return not campo.strip()


def senhas_nao_sao_iguais(senha, senha2):
    """Atalho para não deixar senha vazio ou diferentes"""
    return senha != senha2

