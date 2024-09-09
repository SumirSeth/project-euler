import math

def largest_prime_factor(n):
    largest = 1
    
    # Handle 2 as a special case
    while n % 2 == 0:
        largest = 2
        n = n // 2
    
    # Check odd numbers up to sqrt(n)
    for i in range(3, int(n/2) + 1, 2):
        if n % i == 0:
            largest = i
            print(i)
    
    # If n is still greater than 2, it's prime
    if n > 2:
        largest = n
    
    return largest

num = 600851475143
result = largest_prime_factor(num)
print(result)

