from django.contrib import admin
from .models import(
   Sexo,
   Produto,
   Categoria,
   GastosExrtas,
   Vendas,
   Pessoa,
   EntradaMercadoria,
   fornecedor,
   pessoaFisica,
   pesoaJuridica

)


'''class ClienteFs(admin.ModelAdmin):
    list_display=( 'nome', 'endereco','email', 'telefone')


class estoque(admin.ModelAdmin):
    list_display=( 'nome', 'codigo','estoque')

    def veiculo(self, obj):
        return obj.nome    '''

'''class MovMensalistaAdmin(admin.ModelAdmin):
    list_display=( 'mensalista','dataPaga', 'total')'''

admin.site.register(Sexo)
admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(GastosExrtas)
admin.site.register(Vendas)
admin.site.register(Pessoa)
admin.site.register(EntradaMercadoria)
admin.site.register(fornecedor)
admin.site.register(pessoaFisica)
admin.site.register(pesoaJuridica)

# search_fields =('GastosExrtas',)
 #list_filter= ('GastosExrtas',)


