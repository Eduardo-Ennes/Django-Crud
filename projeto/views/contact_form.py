from django.shortcuts import render, redirect, get_object_or_404
from projeto.forms import contactform
from django.urls import reverse
from projeto.models import contact



def create(request):
    # form_action = reverse('create')
    if request.method == 'POST':
        form = contactform(request.POST)
        context = {
            'formulario': form,
            # 'form_action': form_action
        }
        
        '''
        Logo abaixo fazemos o processo de salvar os dados no banco de dados, is_valid() verifica se não a erros no formulário, se não houver irá salvar as informações.
        Logo em seguida vai redirecionar para a mesma página, para limpar o formulário.
        '''
        if form.is_valid():
            form.save()
            return redirect('create')

            '''
            Faz com que as informações não sejam salvas, sendo armazenadas na variável, logo podemos modificar informações e depois salvar no banco de dados, conforme o exemplo.
            '''
            # contact = form.save(commiti=False)
            # contact.show = False 
            # contact.save()
            
        return render(request, 'create.html', context)
    else:
        form = contactform()
        context = {
            'formulario': form
        }
        return render(request, 'create.html', context)
  


'''
Atualização de dados não deu certo
'''

# def update(request, contato_id):
#     variavel = get_object_or_404(contact, pk=contato_id, show=True)
#     form_action = reverse('projeto:update', args=(contato_id))
#     if str(request.method) == 'POST':
#         form = contactform(request.POST, instance=variavel)
#         context = {
#             'formulario': form,
#             'form_action': form_action
#         }
#         if form.is_valid():
#             contato = form.save()
#             return redirect('create', contato_id=variavel.pk)
#         return render(request, 'create.html', context)
#     else:
#         context = {
#             'formulario': contactform(),
#             'formulario': contactform(instance=variavel),
#             'form_action': form_action
#         }
#         return render(request, 'create.html', context)       