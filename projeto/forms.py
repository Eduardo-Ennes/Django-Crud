from projeto.models import contact
from django import forms 
from django.core.exceptions import ValidationError


'''
Criação de formulário com o ModelForm
'''
class contactform(forms.ModelForm):
    # first_name = forms.CharField(label='Primeiro Nome', help_text='Digitar apenas o prieiro nome',) # É uma forma de trabalhar nos formulários, apresentando uma ajuda por exemplo
    
    class Meta: # A class meta deve sempre ser com letra maiuscula, isso me deu um problema
        model = contact
        fields = ['first_name', 'last_name', 'phone', 'email', 'description', 'category']


    '''
        Para baixo começa a validação de dados dos formulários.  
    '''
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if first_name == last_name:
            msg = ValidationError('The first_name cannot be like the last_name')
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)
        else:
            return super().clean()
      
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name == 'abc':
            self.add_error('first_name', ValidationError('Não digite abc', code='invalid'))
            print('certo')
        else:
            return first_name
    