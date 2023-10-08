from django.contrib import admin
from django.contrib import admin
from . import models

class Cadastro_clienteAdmin(admin.ModelAdmin):
    search_fields = ["Nome", "Endereço", "email", "Telefone", "cpf", "Idade"]
    readonly_fields = ["updated_by", "created_at"]