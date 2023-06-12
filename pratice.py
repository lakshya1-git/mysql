a = 0 , b=1, c
def fib():
    n = int(input("Enter the number to ru upto series"))
    for i in range(0,n):
        c = a +b
        b = c
        a = b
        print(c)
fib()
