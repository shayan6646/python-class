def fib(n):
    if n<0:
        print("Incorrect input")
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
