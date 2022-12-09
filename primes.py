"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if (number_of_primes<1):
        print("0 or negative values are not accepted")

    list = []
    count = 0
    while count<number_of_primes:
        for n in range(2,prime_nums):
            if (prime_nums % n == 0):
                break
            else:
                count+=1
                list.append(prime_nums)
            prime_nums+=1

    return list
