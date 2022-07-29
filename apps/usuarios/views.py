import email
from urllib import request
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from diario.models import Noticia
from diario.views import noticia
from django.contrib import  messages

def cadastro(request):
    """Faz cadastro de usuario """
    if request.method == "POST":
        nome = request.POST["nome"]
        email = request.POST["email"]
        senha = request.POST["senha"]
        senha2 = request.POST["senha2"]
     

        if campo_vazio(nome):
            messages.error(request,"Campo nome não pode ficar em branco!")
            return redirect('cadastro')
        if campo_vazio(email):
            messages.error(request,"Campo email não pode ficar em branco!")
            return redirect('cadastro')
        if campo_vazio(senha):
            messages.error(request,"Campo senha não pode ficar em branco!")
            return redirect('cadastro')
        if campo_vazio(senha2):
            messages.error(request,"Campo senha2 não pode ficar em branco!")
        if senhas_nao_sao_iguais:
            messages.error(request,"As senhas não são iguais!")
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            messages.error(request, "O usuario já tem o cadastro no sistema!")
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request,"Usuario já cadastrado!")
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request,"Usuario cadastrado com sucesso!")
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    """Faz login de usuario"""
    if request.method == "POST":
        email = request.POST["email"]
        senha = request.POST["senha"]
        
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, "Campo email e a senha não pode estar em branco!")
            return redirect('login')
            

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect('dashboard')

    return render(request, 'usuarios/login.html')



def dashboard(request):
    """Dashboard das noticias do usuario"""
    if request.user.is_authenticated:
        id = request.user.id
        noticias = Noticia.objects.order_by('-data_noticia').filter(pessoa=id)

        dados = {
            "noticias": noticias
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')


def logout(request):
    """O usuario faz logout no sistema"""
    auth.logout(request)
    return redirect('index')

def campo_vazio(campo):
    """Atalho para não permitir campos em brancos"""
    return not campo.strip()

def senhas_nao_sao_iguais(senha, senha2):
    """Atalho para não permitir senhas dierentes"""
    return senha != senha2