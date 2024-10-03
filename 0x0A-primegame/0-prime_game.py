#!/usr/bin/python3
"""
Prime Game Module.
"""


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game over multiple rounds.
    Returns:
        str or None: The name of the player who won
        the most rounds ("Maria" or "Ben"),
        or None if there is no clear winner.
    """
    if not isinstance(x, int) or x < 1:
        return None
    if not isinstance(nums, list) or len(nums) != x:
        return None

    max_n = max(nums) if nums else 0
    sieve = [True] * (max_n + 1)
    sieve[0:2] = [False, False]

    # Sieve of Eratosthenes to identify primes up to max_n
    for current in range(2, int(max_n**0.5) + 1):
        if sieve[current]:
            for multiple in range(current*current, max_n + 1, current):
                sieve[multiple] = False

    # Precompute the number of primes up to each index
    prime_counts = [0] * (max_n + 1)
    count = 0
    for i in range(2, max_n + 1):
        if sieve[i]:
            count += 1
        prime_counts[i] = count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 2:
            ben_wins += 1
            continue
        primes_up_to_n = prime_counts[n]
        if primes_up_to_n % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
