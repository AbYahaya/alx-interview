#!/usr/bin/python3
"""
Prime Game: Maria and Ben take turns picking primes optimally
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game after x rounds.

    Parameters:
    x (int): Number of rounds
    nums (list of int): List of `n` for each round

    Returns:
    str: Name of the player with the most wins ("Maria" or "Ben")
         or None if it's a tie.
    """
    if not nums or x < 1:
        return None

    def sieve_of_eratosthenes(max_n):
        """Generate a list of prime numbers up to max_n."""
        is_prime = [True] * (max_n + 1)
        is_prime[0], is_prime[1] = False, False  # 0 and 1 are not prime
        for i in range(2, int(max_n**0.5) + 1):
            if is_prime[i]:
                for multiple in range(i * i, max_n + 1, i):
                    is_prime[multiple] = False
        return is_prime

    # Find the largest number in nums to precompute primes
    max_n = max(nums)
    is_prime = sieve_of_eratosthenes(max_n)

    # Precompute the number of primes up to each number
    primes_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        primes_count[i] = primes_count[i - 1] + (1 if is_prime[i] else 0)

    # Play each round
    maria_wins, ben_wins = 0, 0
    for n in nums:
        if primes_count[n] % 2 == 1:
            maria_wins += 1  # Maria wins if the count of primes is odd
        else:
            ben_wins += 1  # Ben wins if the count of primes is even

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
