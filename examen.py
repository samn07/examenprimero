#realice un algoritmo que permita la entrada de datos por teclado , evalue dicha entrada, separe la entrada
#en numeros y letras eh imprimalos por pantalla
def entradasD (v1):
	if  isalpha(v1):
		print ("entrada esta compuesta por letras", v1)

def entradaE (v2):
	if 	isdigit(v2):
		print ("la entrada esta cmpuesta por numeros",v2)
	
print "ingrese sus nombre "
v1 = raw_input()
v1 = str (v1)

print " ingrese numeros"
v2= raw_input()
v2 = int (v2)

entradasD (v1)
entradaE (v2)
