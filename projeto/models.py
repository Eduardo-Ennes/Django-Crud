from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta: # class Meta deve ser com letra maiusculo, isso me deu um puta problema.
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    profissao = models.CharField(max_length=70)
    def __str__(self): 
        return f'{self.profissao}'

class contact(models.Model):
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    # Caso o banco de dados Category seja apagado, os valores de contact ficaram com o valor NULL.
    
    picture = models.ImageField(blank=True, upload_to='picture/%y/%m/')
    # depende do pillow para funcionar, então devemos baixar o pillow.
    
    own = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.created_date}'
    # Seleciona os campos do banco de dados que serão mostrados na admin do django
