import array as arr
sum = 0
x = arr.array('i', [1,2,3,4,5,6,7])
x.insert(2,0)
 
print('The element in the index 3 of the array is: ', x[3],x)
for i in range(len(x)):
        sum = sum + arr[i]
print(sum)

y =  arr.array('d', [1.5, 2.7, 3.5, 8.2, 6.9])

# to access the index 0 or the first element of the array
print('The element of the array in the index 0 of the float array is: ', y[0])