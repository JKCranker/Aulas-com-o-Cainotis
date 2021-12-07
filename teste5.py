var = input("Digite UM número: ")
lista = []

while var != "fim":


	if var.isnumeric() == False:

		print ("Apenas números")


	else: 

		lista.append (int(var))
		i = len(lista) - 1 

		while (i > 0) and (lista[i] < lista[i - 1]) :
			aux = lista[i]
			lista[i] = lista[i - 1]
			lista[i - 1] = aux
			i = i - 1

		print (lista)

	var = input("Digite outro número: ")








