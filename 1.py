"""first part only
lst = []
with open('Main.txt') as small_pf:
    tmp_list = []
    for line in small_pf:
        line = line.rstrip("\n")
        if line == "":
            lst.append(tmp_list)
            tmp_list = []
        else:
            tmp_list.extend(line.split())

    if tmp_list:  # add last one
        lst.append(tmp_list)

print(lst)
max=0
sum=0
for i in range(len(lst)):
	for j in range(len(lst[i])):
		lst[i][j]=int(lst[i][j])
for i in range(len(lst)):
	for j in range(len(lst[i])):
		sum+=lst[i][j]
	if(sum>=max):
		max=sum
	sum=0
print(max)
"""
lst = []
with open('Main.txt') as small_pf:
    tmp_list = []
    for line in small_pf:
        line = line.rstrip("\n")
        if line == "":
            lst.append(tmp_list)
            tmp_list = []
        else:
            tmp_list.extend(line.split())

    if tmp_list:  # add last one
        lst.append(tmp_list)

array=[]
sum=0
for i in range(len(lst)):
	for j in range(len(lst[i])):
		lst[i][j]=int(lst[i][j])
for i in range(len(lst)):
	for j in range(len(lst[i])):
		sum+=lst[i][j]
	array.append(sum)
	sum=0
print(array)
array.sort(reverse=1)
print(array)
max=array[0]
max2=array[1]
max3=array[2]
print(max+max2+max3)