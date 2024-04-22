'''
Common numbers-related algorithms

Contents:
- isPrime  # Check if a number is prime
- factors  # Returns all factors of n
- prime_factors  # Returns all prime factors of n in a dict
- sieve  # Sieve of Eratosthenes
- absolute  # (prefix sum) Calculate absolute diff between each number and every other number
'''


from math import sqrt
from collections import defaultdict

# Check if a number is prime
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n+0.5))+1):
        if n % i == 0:
            return False
    return True

# Returns all factors of n
def factors(n):
    factors = []
    big_factors = []
    i = 2
    k = 1
    while i * i <= n:
        if n % i == 0:
            factors.append(i ** k)
            if i != n // i:
                big_factors.append(n // i)
        i += 1
    return factors + list(reversed(big_factors))

# Returns all prime factors of n in a dict
def prime_factors(n):
    factors = defaultdict(int)
    while n % 2 == 0:
        factors[2] += 1
        n = n // 2
    i = 3
    while i <= n:
        while n % i == 0:
            factors[i] += 1
            n = n // i
        i += 2
    return dict(factors)

# Sieve of Eratosthenes. Return a list of all prime numbers sorted.
def sieve(num):
    prime = [True for i in range(num+1)]  # boolean array
    p = 2
    while (p * p <= num):
        # Mark all multiples of this prime 
        if (prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    # Print all prime numbers
    primes = []
    for p in range(2, num+1):
        if prime[p]:
            primes.append(p)
    return primes

# Calculate the absolute difference between a number and all other numbers using a presum, ie.
# res[i] = abs(nums[i] - nums[0]) + abs(nums[i] - nums[1]) + ... + abs(nums[i] - nums[n-1])
def absolute(nums):
    n = len(nums)
    presum = [nums[0]] * n
    # Inclusive presum, ie presum[i] = nums[0]+..+nums[i]
    for i in range(1, n):
        presum[i] = presum[i-1] + nums[i]
    res = [0] * n
    for i in range(n):
        # Absolutes on the left side
        # res[i] += (i+1) * nums[i] - presum[i]
        # Absolutes on the right side
        # res[i] += presum[-1] - presum[i] - (n-1 - i) * nums[i]

        # Combining both, this is the magic equation. There is no reason to use this
        res[i] = presum[-1] - 2 * presum[i] + (2 + 2 * i -n) * nums[i]
    return res

print(absolute([1,2,3,4,5,6,7,8,9,10]))


