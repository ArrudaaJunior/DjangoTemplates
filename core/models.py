# Importações do Django
from django.db import models


# Modelo do Produto
class Produto(models.Model):

    # Dados do Produto
    nome_produto = models.CharField('Nome', max_length=100)
    preco_produto = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque_produto = models.IntegerField('Quantidade de Produto em Estoque')

    # Função para apresentar o nome do objeto produto no fórmulario.
    def __str__(self):
        return self.nome_produto


# Modelo do Cliente
class Cliente(models.Model):

    # Dados do Cliente
    nome_cliente = models.CharField('Nome do Cliente', max_length=100)
    sobre_nome_cliente = models.CharField('Sobre Nome do Cliente', max_length=100)
    email_cliente = models.EmailField('Email do CLiente', max_length=100)

    # Função para apresentar o nome e sobren ome do objeto cliente no fórmulario.
    def __str__(self) :
        return f'{self.nome_cliente} {self.sobre_nome_cliente}'