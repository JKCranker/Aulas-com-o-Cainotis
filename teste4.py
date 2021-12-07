var = input ("Digite sua idade: ")

#isnumeric = checa se o str é um número intero positivo, dando apenas "True" ou "False" como resposta
#str = string, conjunto de caracteres
while var.isnumeric() == False:
	var = input ("Digite sua idade: ")

print ("Sua idade é:", var)