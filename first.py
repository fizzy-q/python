n = int(input("Enter a number: "))
def factorial (n):
    if n == 0:
        return int(1)
    else:
        return n * factorial(n-1)
print("factorial is: " , factorial(n))