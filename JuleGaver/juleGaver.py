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
	gaver = input("Hvor mange gaver fik de Anna, Laura og Oscar >> ")
	gaverSplit = gaver.split()
	AnnaAntalGaver = int(gaverSplit[0])
	LauraAntalGaver = int(gaverSplit[1])
	OscarAntalGaver = int(gaverSplit[2])

	if AnnaAntalGaver <= 100 and LauraAntalGaver <= 100 and OscarAntalGaver <= 100:
		print("Success")
	else:
		print("Der må maks gives 100 gaver!")

if __name__ == "__main__":
	main()