N = int(input())
m = 1

def factorial(i):
    global m,N

    if i == N:
        return m
    
    m *= (i+1)
    return factorial(i+1)

print(factorial(0))