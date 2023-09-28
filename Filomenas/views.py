from django.shortcuts import render

# Sem cadastro

def index(request):
    return render (request, 'Filomenas/index.html')


# Com login

def index_logado(request):
    return render (request, 'Logado/index_logado.html')

def Minha_conta (request):
    return render (request, 'Logado/minha_conta.html')