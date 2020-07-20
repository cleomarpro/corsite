from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from datetime import tade
#import math



class Pessoa(models.Model): # CLASSE PAI
    nome = models.CharField(max_length=70)
    endereco = models.CharField(max_length=80, blank=True)
    numero=models.CharField(max_length=10, blank=True)
    bairo = models.CharField(max_length=80, blank=True)
    cidade = models.CharField(max_length=80, blank=True)
    complemento = models.CharField(max_length=80, blank=True)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100, blank=True)

    def __str__(self): # METODO CONSTRUTOR
        return str(self.nome) + ' - ' + str(self.telefone)


class fornecedor(Pessoa): # SUB-CLASSE DA CLASSE PAI Pessoa
    cnpj = models.CharField(max_length=20)

    def __str__(self): # METODO CONSTRUTOR
        return str(self.nome) + ' - ' + str(self.cnpj)

class Sexo (models.Model):
    sexo = models.CharField(max_length=11)

    def __str__(self): # METODO CONSTRUTOR
       return self.sexo



class pessoaFisica(Pessoa): # SUB-CLASSE DA CLASSE PAI Pessoa
    data_de_Nacimento = models.CharField(max_length=10, blank=True)
    CPF = models.CharField(max_length=20)
    sexo = models.ForeignKey(Sexo, verbose_name='Sexo', on_delete=models.CASCADE, default=1)

    def __str__(self): # METODO CONSTRUTOR
        return str(self.nome) + ' - ' + str(self.CPF)


class pesoaJuridica(Pessoa): # SUB -LASSE DA CLASSE PAI Pessoa
    cnpj = models.CharField(max_length=20)

    def __str__(self): # METODO CONSTRUTOR
        return str(self.nome) + ' - ' + str(self.cnpj)


class Categoria (models.Model):
    nome = models.CharField(max_length=50,blank=True)

    def __str__(self): # METODO CONSTRUTOR
       return self.nome



class Produto (models.Model):
    nome = models.CharField(max_length=70,  blank=True)
    categoria = models.ForeignKey(Categoria, verbose_name='Categoria', on_delete=models.CASCADE, default=1)
    codigo = models.CharField(max_length=13,  blank=True)
    valor = models.DecimalField(max_digits=9, decimal_places= 2)
    estoque = models.IntegerField(max_length=12,  default=0)

    def __str__(self): # METODO CONSTRUTOR
       return str(self.nome) + ' - ' + str(self.codigo)+ ' - ' + str(self.estoque)


class Vendas (models.Model):
    produto = models.ForeignKey(Produto, verbose_name='Produto', on_delete=models.CASCADE, default=1)
    quantidade = models.IntegerField(max_length=12,  default=0)
    valor = models.DecimalField(max_digits=9, decimal_places= 2)
    dataHora = models.DateTimeField(default=timezone.now)

    def __str__(self): # METODO CONSTRUTOR
       return str(self.produto.nome )+ ' - ' + str(self.produto.codigo)+ ' - ' + str(self.quantidade)+ ' - ' + str(self.produto.valor)


class EntradaMercadoria(models.Model):
    produto = models.ForeignKey(Produto, verbose_name='Produto', on_delete=models.CASCADE, default=1)
    Fornecedor = models.ForeignKey(fornecedor, verbose_name='fornecedor', on_delete=models.CASCADE, default=1)
    valor = models.DecimalField(max_digits=9, decimal_places= 2)
    quantidade = models.IntegerField(max_length=12,  default=0)
    dataHora = models.DateTimeField(default=timezone.now)

    def __str__(self):# METODO CONSTRUTOR
       return str(self.produto.nome)+ ' - ' + str(self.produto.estoque) + ' - ' + str(self.produto.codigo) + ' - ' + str(self.valor)+ ' - ' + str(self.dataHora)

    def incerir_stoque(self,):
        return self.Produto.estoque + self.quantidade




class GastosExrtas (models.Model):
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=9, decimal_places= 2)
    dataHora = models.DateTimeField(default=timezone.now)


    def __str__(self):# METODO CONSTRUTOR
       return str(self.valor) + ' - ' + str(self.descricao)

class Caixa (models.Model):
    produto = models.ForeignKey(Produto, verbose_name='Produto', on_delete=models.CASCADE, default=1)
    quantidade = models.IntegerField(max_length=12,  default=0, verbose_name = 'Quantidade')
    valor = models.DecimalField(max_digits=9, decimal_places= 2)
    dataHora = models.DateTimeField(auto_now = True )
    usuario = models.ForeignKey(User, on_delete= models.CASCADE)

    class Meta:
        db_table = 'caixa'

'''

  python manage.py makemigrations (comando para migrar para o django)
  python manage.py migrate  (comanto para moigra para o banco)

  mensalista = models.ForeignKey(Mensalista, on_delete=models.CASCADE)
  detalhe = models.TextField()
  email = models.EmailField()
  pago= models.BooleanField(default=False)

'''
