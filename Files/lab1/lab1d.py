#Calvin Lui 84152100 and Mark Lewis 10171060. Ics 31 lab sec 2.
def factorial (n: int) -> int:
    ''' Compute n! (n factorial) '''
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)
assert factorial(0) == 1 
assert factorial(5) == 120 

print("10! is", factorial(10))
print("100! is", factorial(100))
print("32! is", factorial(32))
print(factorial(12*2))
#print(factorial(factorial(13**2)))
#print(factorial(factorial(50)))
