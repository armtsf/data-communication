import random

def add_noise(noiseless):
	noisy = ""
	for n in noiseless:
		r = random.uniform(0, 1)
		if r < 0.1:
			noisy += str(1 - (ord(n) - 48))
		else:
			noisy += n
	return noisy
