from random import randint
listaPalavras = [
"arvore","casa" ]

listaDicas = [
"tem folhas...","serve de abrigo..." ]

# Escolhe uma palavra da lista
x = randint(0,len(listaPalavras) - 1) # é -1 porque a lista começa em 0, se não tiver o -1 vai passar o tanto de posições
escolhida = listaPalavras[x]

#isso vai separar as letras da palavra, será usado em breve
palavra =[escolhida]

for c in range(0,len(escolhida)):
    print(escolhida[c])




#apenas outro modo de separar a palavra
# p = 0
# while p < len(escolhida):
#     print(escolhida[p])
#     p += 1


# for c in range (0, len(listaPalavras)): #o "c" seria como o p, onde p = p+1, o for faz isso automaticamente, conta do 0 até o tamanho final da lista