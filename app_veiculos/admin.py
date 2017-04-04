from django.contrib import admin

# Register your models here.
from app_veiculos.models import TipoDeVeiculo, MarcaDoVeiculo, Veiculo

admin.site.register(TipoDeVeiculo)

admin.site.register(MarcaDoVeiculo)

admin.site.register(Veiculo)
