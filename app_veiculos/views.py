from django.shortcuts import render

# Create your views here.
from app_veiculos.models import Veiculo


def index(request):

    consulta_ao_banco = Veiculo.objects.all()

    return render(request, 'index.html',
                  {'consulta_ao_banco': consulta_ao_banco})
