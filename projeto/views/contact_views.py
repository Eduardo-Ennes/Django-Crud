from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from projeto.models import contact

def index(request):
    print('Usuário: ', request.user)
    contatos = contact.objects.filter(show=True)

    paginator = Paginator(contatos, 10) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'index.html', context)


def search(request):
    search_value = request.GET.get('q', '').strip()
    if search_value == '':
        return redirect('index')
    
    contatos = contact.objects.filter(show=True).filter(
        Q(first_name__icontains=search_value)|
        Q(last_name__icontains=search_value)|
        Q(phone__icontains=search_value)|
        Q(email__icontains=search_value)|
        Q(id__icontains=search_value)
        ).order_by('-id')
    # este é um código que busca no banco de dados todos os contatos que estão ATIVOS, no segundo filter será usado no search para filtragem de busca
    
    '''Aqui são as configurações para implementar o paginator, devido a essa implementação algumas variaveis tiveram que mudar de nome.'''
    paginator = Paginator(contatos, 10) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj
    }
    return render(request, 'index.html', context)


def Contact(request, Contact_id):
    # single_contact = contact.objects.get(pk=contato_id)
    single_contact = get_object_or_404(contact, pk=Contact_id, show=True) #faz a mesma coisa que o código acima, porem só irá buscar contatos que estão ativos, caso seja falso esse código encaminha para um página 404 padrão do django
    
    '''Aqui não foi necessário colocar as configurações do paginator'''
    
    context = {
        'contact': single_contact
    }
    return render(request, 'Contact.html', context)