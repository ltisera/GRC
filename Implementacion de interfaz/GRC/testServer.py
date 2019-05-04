class Calculadora():
	def __init__(self):
		pass
	
		
	def Sumar(self, num1, num2):
		return num1 + num2

def testCalculadora():
	calc = Calculadora()

	if(calc.Sumar(3,5) != 8):
		print("error")
	else:
		print("prueba superada")

	if(calc.Sumar(4,5) != 9):
		print("error")
	else:
		print("prueba superada")



if __name__ == '__main__':
	testCalculadora()
	print("Fin de test")

