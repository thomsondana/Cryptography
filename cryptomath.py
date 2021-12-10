import random
import math

# The gcd function takes two integers and finds the greatest common divisor
def gcd(a, b):
    # swap to make a be the largest value
    if a < b:
        temp = a
        a = b
        b = temp
    # gcd algo using euclidean
    while b != 0:
        q = a // b
        r = a % b
        a = b
        b = r
    return a

# The extended gcd uses extended euclidean to write the gcd as a linear
# combination of a and b
def extended_gcd(a, b):
    # swap to make a be the largest value
    if a < b:
        temp = a
        a = b
        b = temp

    # required initial EE values
    x0, y0 = 0, 1
    x1, y1 = 1, 0
    # extended euclidean aglo
    while b != 0:
        q = a // b
        r = a % b
        linearX = x0 - x1 * q
        linearY = y0 - y1 * q
        x0, y0 = x1, y1
        x1, y1 = linearX, linearY
        a, b = b, r
    return a, x0, y0

# Find the modular inverse of a number using extended gcd
def mod_inverse(alpha, mod):
    # get extended gcd
    gcd, x, y = extended_gcd(mod, alpha)
    # if gcd is not 1 then there is an inverse
    if gcd != 1:
        #print('No possible inverse')
        return -1
    else:
        return x % mod

# find all primitive roots, numbers that are generators for all power p-1
def primitive_roots():
    p = int(input("Enter a prime number: "))
    g = set()
    # check each number between 1 and p
    for i in range(1, p):
        # use sets since they contain unique elements
        h = set()
        for j in range(1, p):
            h.add(pow(i, j, p))
        # if h has p-1 elements then it is a root
        if len(h) == p - 1:
            g.add(i)
    print('\n', sorted(g), '\n')

# check if a value is prime
def isprime(n):
    success = True
    # special case for ints less than 3
    if n < 3:
        if n != 1:
            success = True
        else:
            success = False
    else:
        # case for even numbers
        if n % 2 == 0:
            success = False
        else:
            d = n - 1
            # get usable d value for miller rabin
            while(d % 2 == 0):
                d //= 2

            # default iteration is set to 10
            for i in range(0, 10):
            # use miller rabin to check prime
                if(miller_rabin(d, n) == False):
                    success = False

    return success

# Miller rabin is the method used to determine if a number is prime
def miller_rabin(d, n):
    # get random value a in range 1, n-4
    a = 2 + random.randint(1, n-4)
    # x is a power mod n
    x = pow(a, d, n)
    # if x is 1 or n-1 we're done, n is prime
    if x == 1 or x == n-1:
        return True

    # run through every value till d = n-1
    while(d != n-1):
        # redo x as a power mod n
        x = (x*x) % n
        # update d
        d = d * 2

        # check x to be 1 and n-1 again
        if x == 1:
            return False
        if x == n-1:
            return True

    return False

# Function to get a random prime in range 2^(b+1) - 1 and 2^b + 1
def randPrime(b):
    q = pow(2, b+1) - 1
    p = pow(2, b) + 1
    primes = []

    # run through all ints in range and check if it's prime
    for i in range(p, q):
        if isprime(i):
            # if prime append
            primes.append(i)

    # use the choice function from random library to get random val from primes
    rand = random.choice(primes)
    return p, q, rand

# Entrance function for three factoring methods
def factor():
    # get composite number and int to represent algo choice
    n = int(input("Enter a composite number to factor: "))
    m = int(input("Enter 1 for Fermat, 2 for Pollard rho, or 3 for Pollard p-1: "))
    if m == 1:
        fermat(n)
    elif m == 2:
        pollard_rho(n)
    elif m == 3:
        pollard_p(n)
    else:
        print("Invalid input")

# fermat's factorization formula described in book
def fermat(n):
    # initial values are ceil of square root of n and a^2 - n
    a = math.ceil(math.sqrt(n))
    b = a**2 - n
    sqB = int(math.sqrt(b))

    # while b is not a perfect square add one to a and recalculate b
    while math.sqrt(b) != sqB:
        a = a + 1
        b = a**2 - n
        sqB = int(math.sqrt(b))

    # get factors as a - sqrt(b)
    factor1 = a - math.sqrt(b)
    factor2 = n / factor1
    print('Factors: ', factor1, factor2)

# Pollar rho algo also described in book
def pollard_rho(n):
    # initial values of 2, 2, 1
    a = 2
    b = 2
    d = 1

    # continue running while d=1
    while d == 1:
        # recalculate a, b, d based on the g function
        a = g(a, n)
        b = g(g(b, n), n)
        d = gcd(abs(a-b), n)

    # if d is n at the end then algo failed
    if d == n:
        print('Unable to find factors')
    # else d is a factor
    else:
        print('Factors: ', d, int(n/d))

# Helper function for pollard rho, return a^2 + 1 mod n
def g(a, n):
    return (a**2 + 1) % n

# The pollar p-1 factorization algo as seen in book
def pollard_p(n):
    # start with b as 2 and user input upper bound
    b = 2
    B = int(input('Enter the upper bound for algo: '))

    # run through all values between 2 and bound
    for i in range(2, B):
        # b is updated as a mod power
        b = pow(b, i, n)
        # d is gcd of b-1 and n
        d = gcd(b-1, n)

        # if d is not 1 or n then a factor has been found
        if 1 < d and d < n:
            print('Factors: ', d, int(n/d))
            break

# Shank's square forms factorization algorithm, the equations and updates
# where followed from the Shanks' square form Wikipedia page
def shanks_square():
    # get the composite number and the small multiplier
    N = int(input("Enter an odd integer that is not prime: "))
    # mulitplier has an effect on algo but not sure how to describe it
    k = int(input("Enter a small multiplier integer: "))
    # set initial values for Ps and Qs as specified in algo
    P0 = math.floor(math.sqrt(k*N))
    Pminus1 = P0
    Pi = 0
    Qminus1 = 1
    Qi = k*N - P0**2
    Qplus1 = 1.5
    sqrQ = int(math.sqrt(Qi))

    # check if the composite is already a square, exit if it is
    s = int(math.sqrt(N))
    if s*s == N:
        print("Factors: ", s, s)
        return

    i = 0
    print("Cycle Forward\ni  Pi  Qi  bi")
    print(i, P0, Qminus1)

    # while Qi is not a perfect square
    while sqrQ != math.sqrt(Qplus1):
        i += 1
        # calculate the bi, Pi, and Qi+1
        bi = math.floor((P0 + Pminus1)/Qi)
        Pi = bi * Qi - Pminus1
        Qplus1 = Qminus1 + bi * (Pminus1 - Pi)

        # store Pi-1, Pi, Qi, Qi+1 for next iteration as they're used in calculations
        savePm1 = Pminus1
        Pminus1 = Pi
        Qminus1 = Qi
        Qi = Qplus1
        sqrQ = int(math.sqrt(Qplus1))

        print(i, Pi, Qminus1, bi)

    #done with forward cycle now change initial b, P, Q values for reverse cycle
    Pminus1 = savePm1
    b0 = math.floor((P0 - Pi)/math.sqrt(Qplus1))
    P0 = b0 * math.sqrt(Qplus1) + Pi
    Pminus1 = P0
    Q0 = math.sqrt(Qplus1)
    Qminus1 = Q0
    Qi = (k*N - P0**2) / Q0
    Pminus2 = 0

    i = 0
    print("Reverse cycle\ni  Pi  Qi  bi")
    print(i, P0, Q0, b0)

    # cycle till pi and pi-1 are equal
    while Pi != Pminus2:
        i += 1
        # calculate bi, pi, qi for new i
        bi = math.floor((P0 + Pminus1)/Qi)
        Pi = bi * Qi - Pminus1
        Qplus1 = Qminus1 + bi * (Pminus1 - Pi)

        # save pi-1, pi, qi, qi+1 for use in i+1 calculations
        Pminus2 = Pminus1
        Pminus1 = Pi
        Qminus1 = Qi
        Qi = Qplus1

        print(i, Pi, Qminus1, bi)

    # after reverse cycle exits the factor should be the gcd of Pi and N
    factor = gcd(N, Pi)

    # If the gcd is 1 or N then the algo failed. Otherwise a factor has been found
    if factor != 1 and factor != N:
        print("Factors: ", factor, N/factor)
    else:
        print("Shanks' square forms failed to find a factor")
