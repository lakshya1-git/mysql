arr = [10, 89, 9, 56, 4, 80, 8]
Sum = 0

for i in range(len(arr)):
   Sum = Sum + arr[i]
print (Sum)
for i in range(len(arr)):
   if (arr[0] < arr[i]):
                arr[0] = arr[i]
print(arr[0])