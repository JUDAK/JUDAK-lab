num = input()

arr = []
for i in range(num):
	arr.append(input())

arr.sort()

for i in range(num):
	print arr[i]
