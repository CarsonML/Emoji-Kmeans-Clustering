import random
data = open("data.txt", "r")
lookupdata = open("emoji_lookup.tsv", "r")
contents = data.read()
lookupcontents = lookupdata.read()
contents = contents.split("\n")
lookupcontents = lookupcontents.split("\n")
for x in range(0,len(lookupcontents)):
	lookupcontents[x] = lookupcontents[x].split("\t")

for x in range(0,len(contents)):
	contents[x] = contents[x].split(" ")

values = {}
lookupvalues = {}
for x in range(0,len(lookupcontents)):
	lookupvalues[lookupcontents[x][0]] = lookupcontents[x][1:len(lookupcontents[x])]
for x in range(0,len(contents)):
	values[contents[x][0]] = contents[x][1:len(contents[x])]
for thing in values:
	if thing != "emojiCode":
		for x in range(0, len(values[thing])):
			values[thing][x] = float(values[thing][x])
	#values[thing] = 0
#print (values["eoji1f602"])

def randompoints(x):
	points = {}
	for y in range(0, x):
		rvalue = []
		for z in range(0, 299):
			rvalue.append(random.uniform(-.2, .2))
		points[y] = rvalue
	return points
def comparepoints(rand, values):
	closedict = {}
	test = [0]
	for item in values:
		if item != "emojiCode" and item:
			#test[0] = values[item][0]
			
			#return values[item][0]
			distances = []
			distdict = {}
			for x in range(0,len(rand)):
				dist = 0
				for y in range(0, 299):
					dist = dist + (values[item][y] - rand[x][y])**2
				dist = dist**.5
				distances.append(dist)
			closest = distances.index(min(distances))
			closedict[item] = closest
	return closedict
	
	#el test[1]
	#return[test]
	
def movepoints(rand, close, values):
	totalchecker = []
	newrand = {}
	for z in range(0,300):
		totalchecker.append(0)
	for item in rand:
		counter = 0
		total = []	
		for y in range(0,300):
			total.append(0)
		for thing in close:
			if close[thing] == item:
				counter = counter + 1
				#total = [5,5,5]
				for x in range(0,300):
					total[x] = total[x] + values[thing][x]
		'''if counter == 0:
			rvalue = []
			for z in range(0, 299):
				rvalue.append(random.uniform(-.01, .01))
			
			total = rvalue'''
		for z in range(0,300):
			if counter > 0:
				total[z] = total[z]/counter
			else:
				total[z] = 0
		if total != totalchecker:
			newrand[item] = total
	return newrand
def compare(dict1, dict2):
	n = True
	for thing in dict1:
		if dict1[thing] != dict2[thing]:
			n = False
	return n


def iterate():
	n = False
	points = randompoints(15)
	oldpoints = points
	while not n:
#print (points[2][0])
		closest = comparepoints(points, values)
		npoints = movepoints(points, closest, values)
		if compare(npoints, oldpoints) == True:
			n = False
		else:
			n = True
		oldpoints = npoints

	return closest

def display(numpoints, closeval):
	for item in range(0,numpoints):
		emojis = []
		for item2 in closeval:
			if closeval[item2] == item:
				emojis.append(item2)
		print("\n")
		print("group" + str(item + 1) + ":")
		for item3 in emojis:
			print(lookupvalues[item3[4:9]], end=" ")
#cpoints = iterate()
#print(cpoints)
#print (points)

closepoints = iterate()
display(15, closepoints)







