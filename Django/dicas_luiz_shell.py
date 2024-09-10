'''
Trabalhando com o models.

# Importe o módulo
from contact.models import Contact
contact = Contact()

contact.save() 
# para salvar um dado ou uma alteração 

contact = Contact.objects.create() 
# cria um dado, porem, não precisa do save() para salvar a aplicação, já é salvo automaticamente

contact = Contact.objects.get(pk=10) 
# Faz uma busca, mas com o get deverá ter um argunmento para identificar o dado no banco de dados.

"contact.field_name1 = 'Novo valor 1'
contact.field_name2 = 'Novo valor 2'
contact.save()"
# forma de adicionar ou editar dados, mas deve-se colocar o save() para salvar as informções ou alterações.

contact.delete()
# Para deletar um dado do banco de dados

contacts = Contact.objects.all().order_by('-id')
# Seleciona todos os dados ordenados por ordem decrescente

contacts = Contact.objects.filter(**filters).order_by('-id')
# Seleciona dados usando filtros
'''