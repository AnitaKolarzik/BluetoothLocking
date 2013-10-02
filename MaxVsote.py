def izracunajOptVsoto(sezStevil):
	trenutniMax = 0
	koncniMax = 0
	for element in sezStevil:
		if (trenutniMax + element) > 0:
			trenutniMax += element
		else:
			trenutniMax = 0
		#sito za pozitivna stevila
		#stevila v seznamu sestevamo toliko casa dokler ni vsota negativna
		#st. negativno -> ponovno zacnemo sestevati (nadaljujemo pri trenutnem elementu v zanki)
		koncniMax = max(trenutniMax, koncniMax)
		#primerjamo trenutni najvecji sestevek in zadnji najvecji sestevek ()
	return koncniMax