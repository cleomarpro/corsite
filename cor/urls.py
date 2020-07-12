from django.urls import  path
from cor import views

urlpatterns = [

    path('', views.home),
    path('home/', views.home),
   # path('login/', views.login),



    path('listarentradamercadoria/', views.listarentradamercadoria, name= 'cor_listarentradamercadoria'),
    path('entradamercadoria/', views.entradamercadoria, name= 'cor_entradamercadoria'),
    path('entradamercadoria-novo/', views.entradamercadoria_novo, name= 'cor_entradamercadoria_novo'),
    path('entradamercadoria-update/(?P<id>\d+)/', views.entradamercadoria_update, name='cor_entradamercadoria_update'),
    path('entradamercadoria-delete/(?P<id>\d+)/', views.entradamercadoria_delete, name='cor_entradamercadoria_delete'),

    path('listarcliente/', views.listarcliente, name= 'cor_listarcliente'),
    path('cliente/', views.cliente, name= 'cor_cliente'),
    path('cliente-novo/', views.cliente_novo, name= 'cor_cliente_novo'),
    path('cliente-update/(?P<id>\d+)/', views.cliente_update, name='cor_cliente_update'),
    path('cliente-delete/(?P<id>\d+)/', views.cliente_delete, name='cor_cliente_delete'),

    path('listarfornecedor/', views.listarfornecedor, name= 'cor_listarfornecedor'),
    path('fornecedors/', views.fornecedors, name= 'cor_fornecedors'),
    path('fornecedor-novo/', views.fornecedor_novo, name= 'cor_fornecedor_novo'),
    path('fornecedor-update/(?P<id>\d+)/', views.fornecedor_update, name='cor_fornecedor_update'),
    path('fornecedor-delete/(?P<id>\d+)/', views.fornecedor_delete, name='cor_fornecedor_delete'),

    path('sexo/', views.sexo, name= 'cor_sexo'),
    path('sexo-novo/', views.sexo_novo, name= 'cor_sexo_novo'),
    path('sexo-update/(?P<id>\d+)/', views.sexo_update, name='cor_sexo_update'),
    path('sexo-delete/(?P<id>\d+)/', views.sexo_delete, name='cor_sexo_delete'),

    path('listarprodutos/', views.listarprodutos, name= 'cor_listarprodutos'),
    path('produto/', views.produto, name= 'cor_produto'),
    path('produto-novo/', views.produto_novo, name= 'cor_produto_novo'),
    path('produto-update/(?P<id>\d+)/', views.produto_update, name='cor_produto_update'),
    path('produto-delete/(?P<id>\d+)/', views.produto_delete, name='cor_produto_delete'),

    path('categoria/', views.categoria, name= 'cor_categoria'),
    path('categoria-novo/', views.categoria_novo, name= 'cor_categoria_novo'),
    path('categoria-update/(?P<id>\d+)/', views.categoria_update, name='cor_categoria_update'),
    path('categoria-delete/(?P<id>\d+)/', views.categoria_delete, name='cor_categoria_delete'),



    path('listargastos/', views.listargastos, name= 'cor_listargastos'),
    path('gastosExrtas/', views.gastosExrtas, name= 'cor_gastosExrtas'),
    path('gastosExrtas-novo/', views.gastosExrtas_novo, name= 'cor_gastosExrtas_novo'),

    path('listarvendas/', views.listarvendas, name= 'cor_listarvendas'),
    path('vendas/', views.vendas, name= 'cor_vendas'),
    path('vendas-novo/', views.vendas_novo, name='cor_vendas_novo'),

]
