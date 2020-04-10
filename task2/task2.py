from sys import argv


def readPoints(filename):
	arr = []
	amount = 0
	file = open(filename)
	for str in file:
		if ((amount >= 100) and (filename == argv[2])):
			break;
		arr.append([float(str) for str in str.split(' ', 2) ])
		amount += 1
	file.close()
	return arr

def inPolygon(x, y, xp, yp):
    c=0
    for i in range(len(xp)):
        if (((yp[i]<=y and y<yp[i-1]) or (yp[i-1]<=y and y<yp[i])) and \
            (x > (xp[i-1] - xp[i]) * (y - yp[i]) / (yp[i-1] - yp[i]) + xp[i])): c = 1 - c    
    return c


quadrangle = readPoints(argv[1])
points = readPoints(argv[2])

check_par = False

for point in points:
	if (check_par == False):
		for tops in quadrangle:
			if (point == tops):
				print('0')
				check_par = True

	if (check_par == False):
		for i in range(3):
			x = point[0]
			y = point[1]
			x1 = quadrangle[i][0]
			y1 = quadrangle[i][1]
			x2 = quadrangle[i + 1][0]
			y2 = quadrangle[i + 1][1]
			if (((((x - x1)*(y2 - y1)) - (x2 - x1) * (y - y1)) == 0)
				and ((x - x1)*(x - x2) + (y - y1)*(y - y2))<=0):
				print('1')
				check_par = True

	if (check_par == False):
		c = inPolygon(point[0], point[1], [x[0] for x in quadrangle], [y[1] for y in quadrangle])
		if (c == 0):
			print('3')
		else:
			print('2')
	check_par = False