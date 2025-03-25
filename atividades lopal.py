'''
comando = input("Digite o comando: ")

match comando:
    case "iniciar":
        iniciar_jogo()
    case "salvar":
        salvar_jogo()
    case "sair":
        sair()
    case _:
        print("Comando inválido")


# laço de repetição FOR
# for elemento(variavel) in sequecia:
#   print(elemento)


# exemplo
frutas = ['maça', 'banana', 'laranja', 'amora', 'morango', 'cereja']

for fruta in frutas:
    print(fruta)
print(frutas[0])

# conjuto de strings
mensagem = 'Hello World!'

for caractere in mensagem:
    print(caractere)

# tuplas - semalhante a uma lista, mas imutável. Principal diferença é que tuplas utiliza ()
cores = ("vermelho", "azul", "amarelo", "verde")

for cor in cores:
    print("Cor: ",cor)

# dicionario - uma coleção de pares chave-valor
pessoa = {
    "nome": "Ana",
    "idade": 30,
    "profissão": "engenheira"
}

print(pessoa["nome"])

for chave,valor in pessoa.items():
    print(f"{chave}:{valor}")

# dicionario dentro de dicionario
alunos = {
    "123":{
        "nome": "Lucas",
        "idade": 17
    },
    "456":{
        "nome": "Maria",
        "idade": 18
    }
}

for ra, dados in alunos.items():
    print(f"RA:{ra}")
    for chave, valor in dados.items():
        print(f"{chave.capitalize()}:{valor}")

print(alunos["456"]["nome"])

# conjuntos - uma coleção d elementos únicos, mutável, sem ordem específica.
animais = {"gato", "cachorro", "elefante", "gifara"}

for animal in animais:
    print("Animal: ",animal)

# range - um objeto que representa uma sequencia de números, utilizado em loops for para criar intervalos numéricos.
for numero in range(5):
    for numero in range(0, 11,2):
        print(numero)
    print(numero)

# arquivo - ao abrir um arquivo em Python, voce pode iterar pelas linhas ou caracteres do arquivo

nome_arquivo = "D:/FPOO/08 - Aulas/FPOO-Aula6-Arquivo.txt"

with open(nome_arquivo, "r", encoding="utf-8")as arquivo:
    for linha in arquivo:
        print(linha.strip())



print("contagem de 0 a 10!")
for numero in range(0, 11, 2):
    print(numero)

cores = ("vermelho", "azul", "verde", "amarelo")
for cor in cores:
     print("cor", cor)


soma = 0
for num in range(1, 101):
    soma = soma + num
print(soma)


print("tabuada")
soma = 0
tabuada = int(input("insira um numero"))
for num in range(1, 11):
    multiplicacao = num * tabuada
    soma = soma + 1
    print(f"{tabuada} X {soma}={multiplicacao}")
'''


print("lista de numeros")
lista = int(input("insira a quantidade de numeros"))
for num in range






