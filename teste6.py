#programa que eu vou passar um numero var que responde que o numero
#eh primo ou nao, se ele nao for o programa retorma o numero 
#primo antecessor e sucessor e se for primo retorna que e primo

#numero var sera o "limite"

var = int(input("Digite UM número: "))

i = 2

while i * i <= var:

	if var%i == 0:
		# print ("Seu número não é primo")
		break

	i += 1

if i*i > var and var > 1:
	print ("Seu número é primo")

else : 
	print ("Seu número não é primo")