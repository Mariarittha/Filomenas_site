from django.shortcuts import render

# Sem cadastro

def index(request):
    return render (request, 'Visitantes/index.html')

def teste(request):
    return render(request,'Visitantes/form.html')

# Com login

def index_logado(request):
    return render (request, 'Logado/index_logado.html')

def Minha_conta (request):
    return render (request, 'Logado/minha_conta.html')