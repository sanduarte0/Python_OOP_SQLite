#Importa nosso arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa

#Exemplo de uso
alessandro = Pessoa(1, "Alessandro Duarte")
print(alessandro)

#Quero mostrar só o nome
print(alessandro.nome)