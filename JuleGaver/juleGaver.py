AnnaAntalGaver = 0
LauraAntalGaver = 0
OscarAntalGaver = 0

"""
OPGAVE:
De tre søskende Anna, Laura og Oscar, har netop fået deres julegaver. 
Anna bliver sur, hvis både Laura og Oscar har fået flere julegaver end hende. 
Laura bliver sur hvis Anna har fået flere gaver end hende
og Oscar bliver sur hvis Anna eller Laura (eller begge) har fået flere gaver end ham.

Givet antallet af gaver de 3 søskende hver i sær har fået, 
udskriv navnene på den/dem der bliver sure, eller INGEN hvis ingen af de søskende bliver sure.

"""

def main():
	gaver = input()
	gaverSplit = gaver.split()
	StatusAnna = 0
	StatusLaura = 0
	StatusOscar = 0
	AnnaAntalGaver = int(gaverSplit[0])
	LauraAntalGaver = int(gaverSplit[1])
	OscarAntalGaver = int(gaverSplit[2])

	if AnnaAntalGaver <= 100 and LauraAntalGaver <= 100 and OscarAntalGaver <= 100:
		#Anna bliver sur, hvis både Laura og Oscar har fået flere julegaver end hende.
		if AnnaAntalGaver < LauraAntalGaver and AnnaAntalGaver < OscarAntalGaver:
			StatusAnna = 1
			print("Anna")

		#Laura bliver sur hvis Anna har fået flere gaver end hende
		if LauraAntalGaver < AnnaAntalGaver:
			StatusLaura = 1
			print("Laura")

		#Oscar bliver sur hvis Anna eller Laura (eller begge) har fået flere gaver end ham.
		if OscarAntalGaver < AnnaAntalGaver or OscarAntalGaver < LauraAntalGaver:
			StatusOscar = 1
			print("Oscar")
	
		if StatusAnna == 0 and StatusLaura == 0 and StatusOscar == 0:
			print("INGEN")
	else:
		print("Der må maks gives 100 gaver!")

if __name__ == "__main__":
	main()