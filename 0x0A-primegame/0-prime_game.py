#!/usr/bin/python3
"""Prime Game Script"""


def isWinner(x, nums):
    if not nums or x <= 0:
        return None
    
    # Find the maximum number from nums to know the range of primes to generate
    max_n = max(nums)
    
    # Sieve of Eratosthenes to generate primes up to max_n
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(max_n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, max_n + 1, i):
                sieve[j] = False
    
    # Precompute number of prime moves for each n
    prime_moves = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_moves[i] = prime_moves[i - 1] + (1 if sieve[i] else 0)
    
    # Maria wins if the number of prime moves is odd, otherwise Ben wins
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if prime_moves[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))
