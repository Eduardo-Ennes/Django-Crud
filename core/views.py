from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.paginator import Paginator 
from core.forms import Form_Contato, RegisterForm, UserUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from core.models import Contato
from django.db.models import Q
from django.contrib import messages
from django.contrib import auth

'''
Neste projeto não irei usar paginator e search 
'''


def Index(request):
    contatos = Contato.objects.filter(show=True).order_by('-id')
    # Faz uma busca no banco de dados apenas com usuários que estão ativos
    paginator = Paginator(contatos, 10) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'contatos': contatos,
        'page_obj': page_obj
        
    }
    return render(request, 'index.html', context)


@login_required(login_url='Index')
# Essa é uma biblioteca do python que limita o usuário caso ele não esteja logado, nesse caso ele não poderá acessar essa a página renderizada abaixo, o usuário deverá estar logado aonde o login_required estiver limitando.
def Cadastro(request):
    form_action = reverse('cadastro')
    if request.method == 'POST':
        form = Form_Contato(request.POST)
        context = {
                'form': form,
                'form_action': form_action
        }
        '''
        Logo abaixo fazemos o processo de salvar os dados no banco de dados, is_valid() verifica se não a erros no formulário, se não houver irá salvar as informações.
        Logo em seguida vai redirecionar para a de revisão das informações, para caso queira corrigir alguma informação.
        '''
        if form.is_valid():
            
            contato = form.save()
            return redirect('atualizar', contato_id=contato.pk)
            '''
            Nesse caso não estamos salvando as informações diretamente, commit=False faz com que as informações não sejam salvas, logo estamos armazenando as informações dentro de uma variável
            
            contato.owner = request.user -> atrela o cadastro criado ao campo que é uma foreignkey no banco de dados, o usuário so poderá alterar dados dos cadastros dos quais ele criou
            '''
            '''
            Este seria o metodo usado junto a função create para modificar dados de apenas cadastros com os quais o usuário cadastrou. Dar uma olhada na função create para entender melhor o código 
            
            contato = form.save(commit=False)
            contato.owner = request.user
            
            No models está uma explicação do owner detalhada de como funcionou na aplicação
            '''
        
            '''
            outro exemplo usando commit=False
            
            Faz com que as informações não sejam salvas, sendo armazenadas na variável, logo podemos modificar informações e depois salvar no banco de dados, conforme o exemplo.
            
            contact = form.save(commiti=False)
            contact.show = False 
            contact.save()
            '''
        return render (request, 'cadastro.html', context)
    else:
        form = Form_Contato()
        context = {
            'form': form,
            'form_action': form_action
        }
        return render(request, 'cadastro.html', context)
    
    
def Atualizar(request, contato_id):
    contato = get_object_or_404(Contato, pk=contato_id, show=True)
    '''
    contato = get_object_or_404(Contato, pk=contato_id, show=True, owner=request.user)
    
    Esse seria o metodo implantado para que o usuário do posso alterar dados do cadastros com o qual ele criou. Porem, não está funcionando pq eu esqueci de colocar o 'own' no banco de 
    dados
    
    No models está uma explicação do owner detalhada de como funcionou na aplicação
    '''
    form_action = reverse('atualizar', args=(contato_id,))
    if request.method == 'POST':
        form = Form_Contato(request.POST, instance=contato)
        context = {
                'form': form,
                'form_action': form_action
        }
        if form.is_valid():
            contato = form.save()
            return redirect('Index')
        return render (request, 'cadastro.html', context)
    else:
        form = Form_Contato(instance=contato)
        context = {
            'form': form,
            'form_action': form_action
        }
        return render(request, 'cadastro.html', context)


def Contato_individual(request, contato_id):
    single_contact = get_object_or_404(Contato, pk=contato_id, show=True)
    context = {
        'contact': single_contact
    }
    return render(request, 'contato.html', context)


def Deletar(request, contato_id):
    contato = get_object_or_404(Contato, pk=contato_id, show=True)
    '''
    contato = get_object_or_404(Contato, pk=contato_id, show=True, owner=request.user)
    Neste caso acima o owner=request.user funciona da mesma maneira, so poderá deletar o usuário que criou o cadastro daqueles dados. No models está uma explicação detalhada de como funcionou na aplicação
    '''
    confirmation = request.POST.get('confirmation', 'no')
    if confirmation == 'yes':
        contato.delete()
        return redirect('Index')
    return render(request, 'contato.html', { 'contact': contato, 'confirmation': confirmation})


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado com sucesso!') # retorna uma mensagem de sucesso ao se registrar, eu não mandei aparecer na página 
            return redirect('login')
    
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def login_view(request):
    # authenticatipnform é um autenticador de formuláriopadrão do django que usei para autenticar o login do usuário.
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            # esse metodo valida o usuário
            auth.login(request, user)
            # auth loga o usuário no admin
            return redirect('Index')
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


login_required(login_url='Index')
def user_update(request):
    form = UserUpdateForm(instance=request.user)
    if request.method != 'POST':
        context = {
            'form': form
        }
        return render(request, 'register.html', context)
    else:
        form = UserUpdateForm(data=request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            return redirect('Index')
        else:
            context = {
            'form': form
            }
            return render(request, 'register.html', context)
        

@login_required(login_url='Index')
# outra explicaão: login_required renderiza a página abaixo apenas para usuários logados, caso queira limitar as página deverá fazer acima de cada função que renderiza uma página.
def Logouth(request):
    auth.logout(request)
    return redirect('login')


def Search(request):
    search_value = request.GET.get('q', '').strip()
    if search_value == '':
        return redirect('Index')
    
    contatos = Contato.objects.filter(show=True).filter(
        Q(nome__icontains=search_value)|
        Q(sobrenome__icontains=search_value)|
        Q(telefone__icontains=search_value)|
        Q(email__icontains=search_value)|
        Q(id__icontains=search_value)
        ).order_by('-id')
    # este é um código que busca no banco de dados todos os contatos que estão ATIVOS, no segundo filter será usado no search para filtragem de busca
    paginator = Paginator(contatos, 10) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render (request,'index.html', context)