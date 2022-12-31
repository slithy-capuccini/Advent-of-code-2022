"""primera parte
f = open("Main.txt", "r")
lines = f.readlines()
arr_opp = []
for x in lines:
	arr_opp.append(x.split(' ')[0])
arr_me=[]
for x in lines:
	arr_me.append(x.split(' ')[1].rstrip())
f.close()

cont=0
for i in range(len(arr_opp)):
	if(arr_me[i]=="X"):
		cont+=1
		if(arr_opp[i]=="A"):
			cont+=3
		if(arr_opp[i]=="B"):
			cont+=0
		if(arr_opp[i]=="C"):
			cont+=6
	if(arr_me[i]=="Y"):
		cont+=2
		if(arr_opp[i]=="A"):
			cont+=6
		if(arr_opp[i]=="B"):
			cont+=3
		if(arr_opp[i]=="C"):
			cont+=0
	if(arr_me[i]=="Z"):
		cont+=3
		if(arr_opp[i]=="A"):
			cont+=0
		if(arr_opp[i]=="B"):
			cont+=6
		if(arr_opp[i]=="C"):
			cont+=3

print(cont)
"""
f = open("Main.txt", "r")
lines = f.readlines()
arr_opp = []
for x in lines:
	arr_opp.append(x.split(' ')[0])
arr_me = []
for x in lines:
	arr_me.append(x.split(' ')[1].rstrip())
f.close()

cont = 0
for i in range(len(arr_opp)):
	if (arr_me[i] == "X"):
		cont += 0
		if (arr_opp[i] == "A"):
			cont += 3
		if (arr_opp[i] == "B"):
			cont += 1
		if (arr_opp[i] == "C"):
			cont += 2
	if (arr_me[i] == "Y"):
		cont += 3
		if (arr_opp[i] == "A"):
			cont += 1
		if (arr_opp[i] == "B"):
			cont += 2
		if (arr_opp[i] == "C"):
			cont += 3
	if (arr_me[i] == "Z"):
		cont += 6
		if (arr_opp[i] == "A"):
			cont += 2
		if (arr_opp[i] == "B"):
			cont += 3
		if (arr_opp[i] == "C"):
			cont += 1

print(cont)
