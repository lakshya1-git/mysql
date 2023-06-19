def rotate(arr, d, n):
    for _ in range(d):   
        #Inside the rotate function, the outer loop for _ in range(d) performs the rotation d times. The inner loop for j in range(n - 1) shifts the elements of the array to the left by one position. The first element is temporarily stored in 
        # the variable temp, and then each element is replaced by the next element. Finally, the last element of the array is set to the value of temp.
        #In the corrected code, the rotate function takes three parameters: arr (the array to rotate), d (the number of rotations), and n (the size of the array).
        temp = arr[0]
        for j in range(n - 1):
            arr[j] = arr[j + 1]
        arr[n - 1] = temp

arr = [1, 2, 4, 5, 6, 7, 8]
rotate(arr, 2, 7)
print(arr)

