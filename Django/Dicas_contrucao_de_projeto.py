'''
Aplicação django:
1° - pip install django 
2° - pip freeze > requirements.txt
3° - pwd
4° - django-admin startproject nomedapasta .
5° - django-admin startapp nomedoprojeto
6° - settings -> install app -> colocar o nome do projeto
7° - python manage.py runserver
8° - python manage.py startapp nomedaaplicação --> cria uma pasta para suas aplicações 
9° - cria-se as aplicações nas views de cada projeto, depois deve ser importa para a urls.
10° - cria-se uma pasta chamada "templates" em cada pasta do projeto, em seguida cria-se um arquivo html para desenvolver 
11° - python manage.py makemigrations
12° - python manage.py migrate
13° - python manage.py createsuperuser



Identificação de erros no django:
https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status


'''

'''
2°
(Deve-se observar se está na mesma pasta do manage.py)
1° - python manage.py runserver
2° - Isso irá gerar uma pasta para nossos templetes e rodar localmente 
'''

'''
Melhor forma!

3°
Views

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def contato(request):
    return render(request, 'contato.html')
'''

'''
4° - Melhor forma
Urls

from django.contrib import admin
from django.urls import path

from core.views import index, contato

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index), --> raiz do site
    path('contato', contato),
]
'''

'''
5° 
No models.py cria-se o modelo do banco de dados, em seguida: 
Digite: 'python manage.py makemigrations'  
Após digitar, será criado um arquivo na pasta migrations com todo o banco de dados, por padrão é o Sqlite3
'''

'''
7° 
python manage.py migrate
Cria a porra toda
'''

'''
8° 
python manage.py createsuperuser
para criar uma conta no django e administrar os seus projetos

python manage.py changepassword
para trocar a senha no admin 
'''

'''
Aula 29 do basico 
python manage.py shell -> para acessar o shell direto do terminal, podemos fazer manipulações direto com o power shell e também saber sobre uma biblioteca
'''

'''
INTERMEDIÁRIO - COMEÇA AQUI!

intalações: 
pip install django-bootstrap4 -> para instalar o bootstrap 

bootstrap4 deve ser adicionado no (settings -> INSTALLED_APPS)
'''

'''
instalações para p MySql:
pip install MySQL -> instalação do mysql
pip install PyMySQL -> sistema de integração com o mysql
pip install mysqlclient -> responsavel por fazer a integração com o banco de dados
pip install mysql-connector-python. -> essa instalação serve para atualizar o mysqlclient, que faz a integração com o banco de dados.

em seguida devemos configura:
'ENGINE': 'mysql.connector.django'

configuração para se conectar com o banco de dados: 
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'nomedobancodedados',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
'''

'''
Trabalhando com imagens:
pip install pillow 

Settings:
MEDIA_URL = 'media/'
# Esta configuração server para armazenar as imagens enviadas pelo usuário, no banco de dados anão se salva imagens, apenas urls que apontam para as imagens que no caso estarão dentro dessa pasta.

adicionar a urlpatterns:
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
para mostrar imagem 
'''