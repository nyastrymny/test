from sys import argv
import math;
import functools
import numpy



def find_mediana(n):
	center = len(n) // 2
	s = sorted(n)
	return s[center] if len(n) % 2 != 0 else 0.5*(s[center] + s[center - 1])

#не больше 1000 строк
#исправить эту жесть

file = open(argv[1])
n = []
n = [int(i) for i in file]

stats = []
stats.append(numpy.percentile(n, 90))
stats.append(find_mediana(n))
stats.append(max(n))
stats.append(min(n))
stats.append(sum(n) / len(n))


for i in stats:
	print("%.2f" % i)