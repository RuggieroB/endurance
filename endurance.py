'''
Algoritmo di Laboratorio di Programmazione. Alunno: Bucchianico Enrico Ruggiero, 4^Finf.

Algoritmo "endurance.py": Algoritmo che dati in input la quantità di carburante (in galloni) di un aeroplano e 
il consumo orario (in galloni/h), determina la durata massima di volo.
'''

print ("Endurance: \n Determina la durata massima di volo inserendo la quantita' di carburante (in galloni) ed "\
       "il consumo orario (in galloni/h).  \n  \n  ")
carb = input ("Quantita' di carburante (galloni): ")
carb = float (carb)
cons = input ("Consumo orario (galloni/h): ")
cons = float (cons)
if carb < 0:
	print (" \n ERRORE! La quantita' di carburante non puo' essere negativa!")
elif cons <= 0:
	print (" \n ERRORE! Il consumo orario deve essere maggiore di 0!")
else:
	dv = carb / cons
	ore = int (dv)
	dv = dv - ore
	dv = dv * 60
	minuti = int (dv)
	dv = dv - minuti
	dv = dv * 60
	secondi = int (dv)
	print ("Durata di volo: ", ore, "h", minuti, "min", secondi, "sec")
