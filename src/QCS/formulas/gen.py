from random import randint
from sys import maxsize
from os import system

if __name__ == "__main__":
	n: int
	l: int
	s: int
	
	for i in range(1, 181):
		if(i >= 1 and i <= 30):
			n = 25
			l = 108
		elif(i >= 31 and i <= 60):
			n = 30
			l = 129
		elif(i >= 61 and i <= 90):
			n = 35
			l = 151
		elif(i >= 91 and i <= 120):
			n = 40
			l = 172
		elif(i >= 121 and i <= 150):
			n = 50
			l = 215
		elif(i >= 151 and i <= 180):
			n = 80
			l = 344
		
		s = randint(0,maxsize*2 + 1)
		system("cnfgen --seed {} --output {}.cnf randkcnf 3 {} {}".format(s, i, n, l))

	print("All done!")	
