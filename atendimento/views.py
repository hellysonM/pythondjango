from django.shortcuts import render
from atendimento.models import Senha

def index(request):
    return render(request, 'index.html', {'senhas_na_fila' : Senha.objects.all().filter(status_senha=1),'senhas_outras' : Senha.objects.all().filter(status_senha__in=[2,3,4])})
