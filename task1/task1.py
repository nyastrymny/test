from sys import argv
import numpy

def find_mediana(n):
	center = len(n) // 2
	s = sorted(n)
	return s[center] if len(n) % 2 != 0 else 0.5*(s[center] + s[center - 1])

file = open(argv[1])
n = []

i = 0
for str in file:
	if (i < 1000):
		n.append(int(str))
	else:
		break
	i += 1

stats = []
stats.append(numpy.percentile(n, 90))
stats.append(find_mediana(n))
stats.append(max(n))
stats.append(min(n))
stats.append(sum(n) / len(n))


for i in stats:
	print("%.2f" % i)