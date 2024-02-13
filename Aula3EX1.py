quantidade_numeros = 0
soma = 0

while True:
    numero = int(input("Digite um número inteiro (digite 0 para sair): "))
    
    if numero == 0:
        break  
    
    quantidade_numeros += 1
    soma += numero

if quantidade_numeros > 0:
    media = soma / quantidade_numeros
else:
    media = 0

print("Quantidade de números digitados:", quantidade_numeros)
print("Soma dos números:", soma)
print("Média aritmética dos números:", media)