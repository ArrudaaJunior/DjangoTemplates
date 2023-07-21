from django.contrib import admin

from .models import *

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome_produto', 'preco_produto', 'estoque_produto')


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome_cliente', 'sobre_nome_cliente', 'email_cliente')

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
