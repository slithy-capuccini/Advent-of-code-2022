"""primera parte
f = open("Test.txt", "r")
lines = f.readlines()
cont = 0

arr_1 = []
arr_1_1 = []
arr_1_2 = []
arr_2 = []
arr_2_1 = []
arr_2_2 = []
for x in lines:
	arr_1.append(x.split(',')[0])
#print(arr_1)
for x in arr_1:
	arr_1_1.append(x.split('-')[0])
#print(arr_1_1)
for x in arr_1:
	arr_1_2.append(x.split('-')[1])
#print(arr_1_2)
for x in lines:
	arr_2.append(x.split(',')[1].rstrip())
#print(arr_2)
for x in arr_2:
	arr_2_1.append(x.split('-')[0])
#print(arr_2_1)
for x in arr_2:
	arr_2_2.append(x.split('-')[1])
#print(arr_1_1)
cont = 0
execute = True
for i in range(len(arr_1)):
	print(i, arr_1_1[i], arr_2_1[i])
	print(i, arr_1_2[i], arr_2_2[i])
	if (int(arr_1_1[i]) == int(arr_2_1[i])):
		if (int(arr_1_2[i]) == int(arr_2_2[i])):
			execute = False
	if (execute):
		if (int(arr_1_1[i]) >= int(arr_2_1[i])):
			if (int(arr_1_2[i]) <= int(arr_2_2[i])):
				cont += 1
				print("CONTADOR1:", cont)
		if (int(arr_1_1[i]) <= int(arr_2_1[i])):
			if (int(arr_1_2[i]) >= int(arr_2_2[i])):
				cont += 1
				print("CONTADOR2:", cont)
	else:
		cont += 1
		print("CONTADOR3:", cont)
		execute = True
"""
f = open("Main.txt", "r")
lines = f.readlines()
cont = 0

arr_1 = []
arr_1_1 = []
arr_1_2 = []
arr_2 = []
arr_2_1 = []
arr_2_2 = []
for x in lines:
	arr_1.append(x.split(',')[0])
#print(arr_1)
for x in arr_1:
	arr_1_1.append(x.split('-')[0])
#print(arr_1_1)
for x in arr_1:
	arr_1_2.append(x.split('-')[1])
#print(arr_1_2)
for x in lines:
	arr_2.append(x.split(',')[1].rstrip())
#print(arr_2)
for x in arr_2:
	arr_2_1.append(x.split('-')[0])
#print(arr_2_1)
for x in arr_2:
	arr_2_2.append(x.split('-')[1])
#print(arr_1_1)
cont = 0
execute = True
for i in range(len(arr_1)):
	print(i, arr_1_1[i], arr_2_1[i])
	print(i, arr_1_2[i], arr_2_2[i])
	if (int(arr_1_1[i]) >= int(arr_2_1[i]) and int(arr_1_1[i]) <= int(arr_2_2[i]) ):
		cont+=1
		print("CONTADOR1",cont)
	elif (int(arr_1_2[i]) >= int(arr_2_1[i]) and int(arr_1_2[i]) <= int(arr_2_2[i]) ):
		cont+=1
		print("CONTADOR2",cont)
	elif (int(arr_2_1[i]) >= int(arr_1_1[i]) and int(arr_2_1[i]) <= int(arr_1_2[i]) ):
		cont+=1
		print("CONTADOR3",cont)
	elif (int(arr_2_2[i]) >= int(arr_1_1[i]) and int(arr_2_2[i]) <= int(arr_1_2[i]) ):
		cont+=1
		print("CONTADOR4",cont)
print(cont)