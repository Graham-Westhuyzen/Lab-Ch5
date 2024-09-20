# true if n is a prime number, false otherwise
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
  
# print primes less than n
def print_primes(n):
    for i in range(n):
        if is_prime(i):
            print(i, end=' ')
    print()
    
# return a list of primes less than n
def get_primes(n):
    primes = []
    for i in range(n):
        if is_prime(i):
            primes.append(i)
    return