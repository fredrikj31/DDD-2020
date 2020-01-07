"""
ROMER TAL:
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

"""

def insertSymbol(OrderNR, Number):
	if (OrderNR == 1):
		if Number == '1':
			return "I"
		elif Number == '2':
			return "II"
		elif Number == '3':
			return "III"
		elif Number == '4':
			return "IIII"
		elif Number == '5':
			return "V"
		elif Number == '6':
			return "VI"
		elif Number == '7':
			return "VII"
		elif Number == '8':
			return "VIII"
		elif Number == '9':
			return "VIIII"
		



def main():
	inputTal = input()

	splitNumber = list(inputTal)

	splitNumber.reverse()

	print(splitNumber[0])

	if len(splitNumber) == 1:
		print(insertSymbol(1, splitNumber[0]))
	else:
		print("The number contains more digit")


if __name__ == "__main__":
	main()