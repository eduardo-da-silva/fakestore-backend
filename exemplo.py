idade = 10  # int, str, float, bool, list, dict, tuple, set
nome = "Miguel Paes da Silva"
peso = 84.8
casado = False  # True ou False
linguagens = ["Javascript", "Python"]

print(f"idade = {idade}")
print(f"{nome = }")
print(f"{peso = }")
if casado:
    print("Casado")
else:
    print("Solteiro")
# print(casado)
print("Minhas linguagens")
for linguagem in linguagens:
    print(linguagem)

for i in range(10):
    print(i)

for i in range(2, 8):
    print(i)

for i in range(2, 10, 2):
    print(i)

while idade < 30:
    print("Idade é " + str(idade))
    idade += 1  # idade = idade + 1  +=  -=   *=  /=  **=  //=  %=

print("Sobre o nome Miguel Paes da Silva")
print(f"Tamanho da string = {len(nome)}")
print(f"Primeiro elemento = {nome[0]}")
print(f"Segundo elemento = {nome[1]}")
print(f"Último elemento = {nome[-1]}")
print(f"Penúltimo elemento = {nome[-2]}")
print(f"Tudo maiúsculo = {nome.upper()}")
print(f"Tudo minúsculo = {nome.lower()}")
print(f'Quantidade de "a" = {nome.count("a")}')
print(f'Substituir "a" por "o" = {nome.replace("a", "o")}')
print(f"Dividir por espaço = {nome.split(' ')}")
print(f"Linguagens por vírgula = {', '.join(linguagens)}")

carro = {"marca": "ford", "modelo": "Fiesta", "ano": 2018}

print(f"{carro = }")
print(f"Marca = {carro['marca'].capitalize()}")
print(f"Modelo = {carro['modelo']}")
print(f"Ano = {carro['ano']}")


def dar_bom_dia():
    print("Bom dia!")


def saudar(pessoa):
    print(f"Olá {pessoa}!")


def somar(n1, n2):
    return n1 + n2


dar_bom_dia()
saudar(nome)
saudar("Eduardo")
print(somar(10, 20))
