from django.contrib import admin
#from core.models import Caixa
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
   pesoaJuridica,
   Caixa
)


class CaixaAdmin(admin.ModelAdmin):
    list_display=( 'produto', 'quantidade','valor')

    def calculo(self, obj):
        return (self.Produto.estoque + EntradaMercadoria.quantidade)

    search_fields =('produto',)
    list_filter= ('produto',)



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
admin.site.register(Caixa, CaixaAdmin)

# search_fields =('GastosExrtas',)
 #list_filter= ('GastosExrtas',)


