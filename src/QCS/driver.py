#from scipy.special import lambertw
#from math import log, pi, pow
#from functools import cache

n2nq = dict([(25, 13), (30, 14), (35, 14), (40, 15), (50, 16), (80, 18)])

#@cache 
def get_qubit_num(n: int) -> int:
	return n2nq[n]
	#num: float = n * log(2) - (2 * lambertw(pow(2, -5 + n / 2) * pi * pow(log(2), 2) / 1))
	#return round(num / log(2))

if __name__ == "__main__":
	print(get_qubit_num(25))
	#print(get_qubit_num2(23))
	noise_model = NoiseModel.from_backend("ibm_cleveland")
	backend = AerSimulator(noise_model=noise_model)
	
