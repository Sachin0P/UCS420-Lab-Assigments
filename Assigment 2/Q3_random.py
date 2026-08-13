import random
from collections import Counter

ROLL_NO = 1024170302
random.seed(ROLL_NO)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


numbers = [random.randint(100, 900) for _ in range(100)]
print("i. 100 random numbers:")
print(numbers)

odds = [x for x in numbers if x % 2 != 0]
print("ii. Odd count:", len(odds))
print("    Odd numbers:", odds)

evens = [x for x in numbers if x % 2 == 0]
print("iii. Even count:", len(evens))
print("     Even numbers:", evens)

primes = [x for x in numbers if is_prime(x)]
print("iv. Prime count:", len(primes))
print("    Prime numbers:", primes)

counts = Counter(numbers)
value, freq = counts.most_common(1)[0]
print("v. Most frequent number:", value, "| occurs", freq, "time(s)")
