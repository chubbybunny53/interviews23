def isPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = round(n ** 0.5)
    for factor in range (3, maxFactor, 2):
        if (n % factor == 0):
            return False
    return True

#0th prime == 2
#1st prime == 3
def nthPrime(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if (isPrime(guess)):
            found += 1
    return guess

#1st prime == 2
#2nd prime == 2
def nthPrimeTmp(n):
    found = 0
    guess = 0
    while (found < n):
        guess += 1
        if (isPrime(guess)):
            found += 1
    return guess

def isPalindrome(s):
    while (len(s) > 1):
        if (s[0] != s[-1]):
            return False
        s = s[1:-1]
    return True

def nthThreeDigitPrime(n):
    found = 0
    guess = 0
    while found (found <= n):
        guess += 1
        if (isThreeDigitPrime(guess)):
            found += 1
    return guess

def isThreeDigitPrime(n):
    return (isThreeDigit(n) and isPrime(n))

def isThreeDigit(n):
    return (100 <= n <= 999)
