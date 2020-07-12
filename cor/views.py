from .forms import(
    EntradaMercadoriaForm,
    pessoaFisicaForm,
    fornecedorForm,
    ProdutoForm,
    CategoriaForm,
    SexoForm,
    GastosExrtasForm,
    VendasForm

)
#from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import (
EntradaMercadoria,
pessoaFisica,
fornecedor,
Produto,
Categoria,
Sexo,
GastosExrtas,
Vendas

)

def home(request):
    return render(request,'home.html')

def entradamercadoria(request):
    form = EntradaMercadoriaForm()
    entradamercadoria=EntradaMercadoria.objects.all()
    data= {'entradamercadoria': entradamercadoria, 'form':form}
    return render(request,'entradamercadoria.html', data)

def entradamercadoria_novo(request):
    form = EntradaMercadoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('cor_entradamercadoria')

def entradamercadoria_update(request, id):
    data  = {}
    entradamercadoria = EntradaMercadoria.objects.get(id=id)
    form = EntradaMercadoriaForm(request.POST or None, instance=entradamercadoria)
    data['entradamercadoria'] = entradamercadoria
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('cor_listarentradamercadoria')
    else:
        return render(request, 'cor_entradamercadoria_update.html',data)

def entradamercadoria_delete(request, id):
    data  = {}
    entradamercadoria = EntradaMercadoria.objects.get(id=id)
    if request.method == 'POST':
        entradamercadoria.delete()
        return redirect('cor_listarentradamercadoriae')
    else:
        return render(request, 'delete_confirme.html',data)

def listarentradamercadoria(request):
    entradamercadoria=EntradaMercadoria.objects.all()
    return render(request,'listarentradamercadoria.html', {'entradamercadoria':entradamercadoria })



def cliente(request):
    form = pessoaFisicaForm()
    cliente=pessoaFisica.objects.all()
    data= {'cliente': cliente, 'form':form}
    return render(request,'cliente.html', data)

def cliente_novo(request):
    form = pessoaFisicaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('cor_cliente')

def cliente_update(request, id):
    data  = {}
    cliente = pessoaFisica.objects.get(id=id)
    form = pessoaFisicaForm(request.POST or None, instance=cliente)
    data['cliente'] = cliente
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('cor_listarcliente')
    else:
        return render(request, 'cliente_update.html',data)

def cliente_delete(request, id):
    data  = {}
    cliente = pessoaFisica.objects.get(id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cor_listarcliente')
    else:
        return render(request, 'delete_confirme.html',data)

def listarcliente(request):
    cliente=pessoaFisica.objects.all()
    return render(request,'listarcliente.html', {'cliente':cliente })

def fornecedors(request):
    form = fornecedorForm()
    fornecedors=fornecedor.objects.all()
    data= {'fornecedors': fornecedors, 'form':form}
    return render(request,'fornecedors.html', data)

def fornecedor_novo(request):
    form = fornecedorForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('cor_fornecedors')

def fornecedor_update(request, id):
    data  = {}
    fornecedors = fornecedor.objects.get(id=id)
    form = fornecedorForm(request.POST or None, instance=fornecedors)
    data['fornecedors'] = fornecedors
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('cor_listarfornecedor')
    else:
        return render(request, 'fornecedor_update.html',data)


def fornecedor_delete(request, id):
    data  = {}
    fornecedors = fornecedor.objects.get(id=id)
    if request.method == 'POST':
        fornecedors.delete()
        return redirect('cor_listarfornecedor')
    else:
        return render(request, 'delete_confirme.html',data)





def listarfornecedor(request):
    fornecedors=fornecedor.objects.all()
    return render(request,'listarfornecedor.html', {'fornecedors':fornecedors })





def sexo(request):
    form = SexoForm()
    sexo=Sexo.objects.all()
    data= {'sexo': sexo, 'form':form}
    return render(request,'sexo.html', data)

def sexo_novo(request):
    form = SexoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('cor_sexo')

def sexo_update(request, id):
    data  = {}
    sexo = Sexo.objects.get(id=id)
    form = SexoForm(request.POST or None, instance=sexo)
    data['sexo'] = sexo
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('cor_sexo')
    else:
        return render(request, 'sexo_update.html',data)

def sexo_delete(request, id):
    data  = {}
    sexo = Sexo.objects.get(id=id)
    if request.method == 'POST':
        sexo.delete()
        return redirect('cor_sexo')
    else:
        return render(request, 'delete_confirme.html',data)



def produto(request):
    form = ProdutoForm()
    produto=Produto.objects.all()
    data= {'produto': produto, 'form':form}
    return render(request,'produto.html', data)

def produto_novo(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('cor_produto')


def produto_update(request, id):
    data  = {}
    produto = Produto.objects.get(id=id)
    form = ProdutoForm(request.POST or None, instance=produto)
    data['produto'] = produto
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('cor_produto')
    else:
        return render(request, 'produto_update.html',data)

def produto_delete(request, id):
    data  = {}
    produto = Produto.objects.get(id=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('cor_produto')
    else:
        return render(request, 'delete_confirme.html',data)

def listarprodutos(request):
    produto=Produto.objects.all()
    return render(request,'listarprodutos.html',{'produto': produto})






def categoria(request):
    form = CategoriaForm()
    categoria=Categoria.objects.all()
    data= {'categoria': categoria, 'form':form}
    return render(request,'categoria.html', data)

def categoria_novo(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('cor_categoria')


def categoria_update(request, id):
    data  = {}
    categoria = Categoria.objects.get(id=id)
    form = CategoriaForm(request.POST or None, instance=categoria)
    data['categoria'] = categoria
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('cor_categoria')
    else:
        return render(request, 'categoria_update.html',data)

def categoria_delete(request, id):
    data  = {}
    categoria = Categoria.objects.get(id=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('cor_categoria')
    else:
        return render(request, 'delete_confirme.html',data)




def gastosExrtas(request):
    form = GastosExrtasForm()
    gastosExrtas=GastosExrtas.objects.all()
    data= {'gastosExrtas': gastosExrtas, 'form':form}
    return render(request,'gastosExrtas.html', data)

def gastosExrtas_novo(request):
    form = GastosExrtasForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('cor_gastosExrtas')

def listargastos(request):
    gastosExrtas=GastosExrtas.objects.all()
    return render(request,'listargastos.html', {'gastosExrtas':gastosExrtas })



def vendas(request):
    form = VendasForm()
    vendas=Vendas.objects.all()
    data= {'vendas': vendas, 'form':form}
    return render(request,'vendas.html', data)

def vendas_novo(request):
    form = VendasForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('cor_vendas')

def listarvendas(request):
    vendas=Vendas.objects.all()
    return render(request,'listarvendas.html', {'vendas':vendas })

