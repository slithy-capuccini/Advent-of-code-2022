"""
primera parte
from itertools import groupby
import numpy as np

f = open("Main.txt", "r")
lines = f.readlines()
cont = 0
arr_letter = [
 "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
 "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D",
 "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
 "T", "U", "V", "W", "X", "Y", "Z"
]
arr = []
for x in lines:
	arr.append(x.split('\n')[0])
arr_1 = []
arr_2 = []
arr_final = []
f.close()
size = int(len(arr))
for i in range(size):
	res_first, res_second = arr[i][:len(arr[i]) // 2], arr[i][len(arr[i]) // 2:]
	# printing result
	arr_1.append(res_first)
	arr_2.append(res_second)
print(arr_1)
print(arr_2)
for i in range(len(arr_1)):
	a = list(set(arr_1[i]) & set(arr_2[i]))
	for j in a:
		print(j)
		arr_final.append(j)

for i in range(len(arr_final)):
	for j in range(len(arr_letter)):
		if (arr_final[i] == arr_letter[j]):
			cont += arr_letter.index(arr_final[i]) + 1
print(cont)
"""
from itertools import groupby

f = open("Main.txt", "r")
lines = f.readlines()
cont = 0
arr_letter = [
 "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
 "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D",
 "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
 "T", "U", "V", "W", "X", "Y", "Z"
]
arr_prob = []
arr_prob_2 = []
arr = []
for x in lines:
	arr.append(x.split('\n')[0])
arr_final = []
f.close()
pos = 0
for i in range(int(len(arr))):
	#res_first, res_second = arr[i][:len(arr[i]) // 2], arr[i][len(arr[i]) // 2:]
	# printing result
	if i % 3 != 0 or i == 0:
		arr_prob.append(arr[i])
		print(arr_prob)
	else:
		arr_prob_2 = arr_prob.copy()
		arr_prob.clear()
		arr_prob.append(arr[i])
		arr_final.append(arr_prob_2)
arr_prob_2 = arr_prob.copy()
arr_prob.clear()
arr_prob.append(arr[i])
arr_final.append(arr_prob_2)

print(arr_final)
result_2 = []
result = []
for i in range(len(arr_final)):
	for j in range(len(arr_final[i])):
		a = list(set(arr_final[i][0]) & set(arr_final[i][1]) & set(arr_final[i][2]))
		for j in a:
			print(j)
			result_2.append(j)

for i in range(len(result_2)):
	if (i == 0 or i % 3 == 0):
		result.append(result_2[i])
print(result)
for i in range(len(result)):
	for j in range(len(arr_letter)):
		if (result[i] == arr_letter[j]):
			cont += arr_letter.index(result[i]) + 1
print(cont)
