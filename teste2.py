from random import randint
#[] cria uma lista
y = []
x = 0

# < 15 pra rodar 15x
while x < 15:

	x = x + 1

	#append = adicionar no final da lista
	y.append (randint(0,100))

print (y)

#variavel para poder listar em ordem todo mundo
i = 0

# len = lengh, comprimento
# < len(y) - 1, pq ao ordenar todos os numeros de "y" menos o 1 em ordem crescente, esse sera o maior
while i < len(y) - 1:

	minimo = i
	b = i + 1

	#esse while é para mover o menor numero para o comeco
	while b < len(y):

		if y[minimo] > y[b]:
			minimo = b
		b = b + 1

	# aux = auxiliar
	# uso do aux para nao perder o primeiro numero ao ordenar
	aux = y[i]

	# substituir o primeiro numero pelo menor
	y[i] = y[minimo]
	y[minimo] = aux

	i = i + 1

print (y)