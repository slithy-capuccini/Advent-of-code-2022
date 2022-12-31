"""primera parte
arr_1 = []
arr_final = []
arr_2 = []
verdad = True
max = 0
num = 0


def mover(array, numero, inicio, final):
	numero = int(numero)
	inicio = int(inicio) - 1
	final = int(final) - 1
	for i in range(numero):
		array[final].insert(0, array[inicio][0])
		array[inicio].pop(0)


def get(n):
	arr = [line.split(" ")[n] for line in data]
	return arr


numeros = []
inicios = []
finales = []

with open('Main.txt', 'r') as data:
	for line in data:
		if line == '\n':
			verdad = False
			#arr = [line.split(" ")[n] for line in data]

		else:
			if (verdad):
				arr_1.append(line)
				num += 1
			else:
				numeros.append(line.split(' ')[1])
				inicios.append(line.split(' ')[3])
				finales.append(line.split(' ')[5].rstrip())
for i in arr_1[-1]:
	try:
		if (int(i) > max):
			max = int(i)
	except:
		pass
num -= 1
print(max)
print(num)
print(len(arr_1))
print(arr_1)
arr_1.pop()
print(arr_1)
arr_final = [[0 for x in range(max)] for y in range(len(arr_1))]
for i in range(max):
	for j in range(len(arr_1)):
		print(i, j)
		if (arr_1[j][1 + 4 * i] != ' '):
			arr_final[i][j] = arr_1[j][1 + 4 * i]

for i in range(len(arr_final)):
	arr_final[i] = [j for j in arr_final[i] if j != 0]
print(arr_final)

#print(arr_2[0][5]) how many
#print(arr_2[0][12])where to select
#print(arr_2[0][17])where to move

#move 3 from 9 to 4

for i in range(len(numeros)):
	mover(arr_final, numeros[i], inicios[i], finales[i])
print(arr_final)
word = ""
for i in range(len(arr_final)):
	word += (arr_final[i][0])
print(word)
#arr[0][1]=primera columna
#arr[0][5]=segunda columna
#+4 new columns
#print(arr_2)
"""
arr_1 = []
arr_final = []
arr_2 = []
verdad = True
max = 0
num = 0
arr_sup = []


def mover(array, numero, inicio, final):
	numero = int(numero)
	inicio = int(inicio) - 1
	final = int(final) - 1
	"""for n in range(numero, 0, -1):
		array[final].insert(0, array[inicio][0])
		array[inicio].pop(0)"""
	for i in range(numero):
		array[final].insert(i, array[inicio][0])
		array[inicio].pop(0)


def get(n):
	arr = [line.split(" ")[n] for line in data]
	return arr


numeros = []
inicios = []
finales = []

with open('Main.txt', 'r') as data:
	for line in data:
		if line == '\n':
			verdad = False
			#arr = [line.split(" ")[n] for line in data]

		else:
			if (verdad):
				arr_1.append(line)
				num += 1
			else:
				numeros.append(line.split(' ')[1])
				inicios.append(line.split(' ')[3])
				finales.append(line.split(' ')[5].rstrip())
for i in arr_1[-1]:
	try:
		if (int(i) > max):
			max = int(i)
	except:
		pass
num -= 1
print(max)
print(num)
print(len(arr_1))
print(arr_1)
arr_1.pop()
print(arr_1)
arr_final = [[0 for x in range(max)] for y in range(len(arr_1))]
for i in range(max):
	for j in range(len(arr_1)):
		if (arr_1[j][1 + 4 * i] != ' '):
			arr_final[i][j] = arr_1[j][1 + 4 * i]

for i in range(len(arr_final)):
	arr_final[i] = [j for j in arr_final[i] if j != 0]
print(arr_final)

#print(arr_2[0][5]) how many
#print(arr_2[0][12])where to select
#print(arr_2[0][17])where to move

#move 3 from 9 to 4

for i in range(len(numeros)):
	mover(arr_final, numeros[i], inicios[i], finales[i])
print(arr_final)
word = ""
for i in range(len(arr_final)):
	word += (arr_final[i][0])
print(word)
#arr[0][1]=primera columna
#arr[0][5]=segunda columna
#+4 new columns
#print(arr_2)
