from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




class Profissao(models.Model):
    class meta:
        verbose_name = 'Profissão'
        verbose_name_plural = 'Profissões'
        
    profissao = models.CharField(max_length=70)
    
    def __str__(self):
        return f'{self.profissao}'
    # Seleciona os campos do banco de dados que serão mostrados na admin do django
    
    
class Contato(models.Model):
    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(max_length=500, blank=True)
    show = models.BooleanField(default=True)
    category = models.ForeignKey(Profissao, on_delete=models.SET_NULL, blank=True, null=True)
    # Caso o banco de dados Category seja apagado, os valores de contact ficaram com o valor NULL.
    imagem = models.ImageField(blank=True, upload_to='picture/%y/%m/')
    # depende do pillow para funcionar, então devemos baixar o pillow.
    
    own = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    '''
    É uma foreignkey que atrela os cadastros criados ao usuário, com isso, só poderiamos deletar e atulizar cadastro com os quais o usuário criou. 
    
    forma de usar esta na função create, atualizar, update e no templete dos contatos individuais para que não apareça os botões de update e delete para usuários que não são donos do cadastro. 
    
    Ele é exatamente como vemos, simples.
    '''
    
    
    def __str__(self):
        return f'{self.nome} {self.sobrenome} {self.telefone} {self.email}'
    # Seleciona os campos do banco de dados que serão mostrados na admin do django