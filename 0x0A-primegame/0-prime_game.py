#!/usr/bin/python3
"""Prime Game Script"""


def isWinner(x, nums):
    # Function to determine the winner of the most rounds of the prime game

    max_n = max(nums)

    # Step 1: Precompute primes up to the maximum number using the Sieve of Eratosthenes
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(max_n ** 0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, max_n + 1, i):
                primes[multiple] = False

    # Step 2: Precompute number of prime removals possible for each number up to max_n
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Step 3: Simulate each game round and determine the winner
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Step 4: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
