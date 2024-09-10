'''
dicas para construir um banco de dados.

Id -> já é feito automaticamnte pelo django
CharField -> equivalente ao Varchar no sql
Blanket=True -> Torna o campo opcional 
EmailField -> campo especifico para e-mail
TextField -> para texto grandes e podendo ser sem limitações de caracteres

blank="True" -> Permite que o campo não seja obrigatório
null=True -> permite que o campo seja null e não obrigatório
'''
'''
from django.utils import timezone
"created_date = models.DateTimeField(default=timezone.now)" -> registro do momento em que as informações foram registradas
'''
'''
ForeignKey -> chave estrangeira

!ON_DELETE:!
models.CASCATE -> caso o banco de dados que a ForeignKey estiver linkado for apagado, esse modo irá deletar todos que tiverem o valor relacionado ao outro banco de dados,tomarcuidado porque pode afetar outro banco de dados.

models.SET_NULL -> caso o banco de dados que a ForeignKey estiver linkado for apagado, os campos correspondentes ficaram com valor NULL.
'''