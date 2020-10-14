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

##CAPITULO 3 - INTRODUCAO AS LISTAS
bicycles = ['trek', 'cannondale', 'radline', 'specialized']
print(bicycles)

print(bicycles[0]) #primeira posicao
print(bicycles[0].title()) ## saída mais elegante
print(bicycles[-1].title()) ## Ultimo item da lista

message3 = 'My first bicycle was a ' + bicycles[3].title() + '.'
print(message3)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati' # Substitui o valor da lista que está na posicao 0
print(motorcycles)

motorcycles.append('honda') ## adiciona um item no final da lista
print(motorcycles)

motorcycles.insert(0, 'safra') #insere a string 'safra' na posicao 0
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycles = ['honda', 'yamaha', 'suzuki']
print(popped_motorcycles)
popped_motorcycles.pop() # Remove o último item adicionado na lista
print(popped_motorcycles)

popped_motorcycles.append('suzuki')
popped_motorcycles.append('ducati')
print(popped_motorcycles)
popped_motorcycles.pop(1)
print(popped_motorcycles) #Remove o item informado conforme sua posicao

print(motorcycles)
motorcycles.remove('ducati') ## Remove a string 'ducati
print(motorcycles)

motorcycles.append('ducati')
too_expensive = 'ducati'
motorcycles.remove(too_expensive) ## Remover de acordo com uma variavel
print(motorcycles)
print('A motocicleta removida foi ' + too_expensive)

### EXERCICIO ###

convidados = ['adriano', 'camila', 'bete', 'pablo', 'cassia']

for n in convidados:
    print('Oi ' + n.title() + ', churras no domingo, traga Heineken')

convidados[-1] = 'felipe'
for n in convidados:
    print('Oi ' + n.title() + ', churras no domingo, traga Heineken')

convidados.insert(0, 'sherazade')
print(convidados)

convidados.insert((int(len(convidados) / 2)), 'bono')
print(convidados)

convidados.append('scott')
print(convidados)

for n in convidados:
    print('Oi ' + n.title() + ', churras no domingo, traga Heineken')

desconvidados = ['adriano', 'camila', 'bete', 'pablo', 'felipe']
for d in desconvidados:
    print('Ola ' + d + ', voce foi desconvidado do churras')
    convidados.remove(d)
print(convidados)