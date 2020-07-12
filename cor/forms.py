from django.forms import ModelForm
from .models import EntradaMercadoria, pessoaFisica, fornecedor, Produto, Categoria, Sexo, GastosExrtas, Vendas

class EntradaMercadoriaForm(ModelForm):
    class Meta:
        model = EntradaMercadoria
        fields = '__all__'

class pessoaFisicaForm(ModelForm):
    class Meta:
        model = pessoaFisica
        fields = '__all__'

class fornecedorForm(ModelForm):
    class Meta:
        model = fornecedor
        fields = '__all__'

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class SexoForm(ModelForm):
    class Meta:
        model = Sexo
        fields = '__all__'

class GastosExrtasForm(ModelForm):
    class Meta:
        model = GastosExrtas
        fields = '__all__'

class VendasForm(ModelForm):
    class Meta:
        model = Vendas
        fields = '__all__'

