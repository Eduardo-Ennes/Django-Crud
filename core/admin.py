from django.contrib import admin
from core import models



@admin.register(models.Contato)
class contatoadmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 'sobrenome', 'telefone', 'email', 'own'
    list_editable = 'nome', 'sobrenome', 'telefone', 'email',
    
    '''
    Arquivo complementar para dicas!
    
    list_display = 'id','first_name', 'last_name', 'created_date','show',
    # Cria as colunas que serão apresentadas no admin do django
    
    ordering = '-id', 
    # para ordenar em ordem crescente, para ordenar em decrescente é só colocar o sinal de menos, ex: '-id 
    
    # list_filter = 'created_date', 
    # Cria um filtro para pesquisas usando a data de registro dos usuários 
    
    search_fields = 'id', 'first_name', 'last_name', 
    # Cria uma barra de busca, será filtrado na busca pelos campos digitados no search_fileds
    
    list_per_page = 10
    # Número maximo de dados que serão mostrados a cada página no admin
    
    list_max_show_all = 50
    # Número maximo de dados que serão mostrados a cada página no admin quando selecionar a opção "mostrar todos"
    
    list_editable = 'first_name', 'last_name', 'show',
    # Esse campo ele facilita caso queiramos modificar algum dado no admin, ele ja mostra diretamente no painel as opções selecionadas para editarmos os dados.
    
    # list_display_links = 'id', 'last_name', 
    # Cria um acesso direto ao dados do usuário direto pelo campo desejado 
    '''
    

@admin.register(models.Profissao)
class profissaoadmin(admin.ModelAdmin):
    list_display = 'profissao',
    ordering = 'id',


