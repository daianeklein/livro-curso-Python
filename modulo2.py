## CAPITULO 2
## VARIÁVEIS E TIPOS DE DADOS SIMPLES

print('Hello Python World')

message = 'Hello Pytho World'
print(message)

message = 'Hello Python Crash Course World'
print(message)

# Variáveis
print('Este é um teste - Primeiro exercicio')
mensagem_simples_1 = 'Este é o segundo exercicio'
print(mensagem_simples_1 )

# Strings
name = 'ada lovelace'
print(name.title()) # método title transforma a primeira letra em caixa alta
nome_completo = 'maria dos santos Silva'
print(nome_completo.title())

print(nome_completo.lower()) # Transforma todas as letras em caixa baixa
print(nome_completo.upper()) # Transforma todas as letras em caixa alta
#Util para armazenar dados

# Concatenando strings
first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' + last_name
print(full_name.title())

message2 = 'Hello, ' + full_name.title() + '!'
print(message2)

# Tabulacao e quebras de linhas
print('\tPython') # Tabulacao
print('Eu\nsou\numa quebra de\nlinha') #Quebra de linha
print('Eu sou um\n\tnovo paragrafo')

# Removendo espacos em branco
palavra = 'Python   '
print(len(palavra))
palavra = palavra.rstrip() ## Remove os caracteres em branco do lado direito
print(len(palavra))

palavra2 = '  Python'
print(len(palavra2))
palavra2 = palavra2.lstrip() ## Remove os caracteres em branco do lado esquerdo
print(len(palavra2))

##NUMEROS
age = 23
message = 'happy ' + str(age) + 'rd Birthday'
print(message)