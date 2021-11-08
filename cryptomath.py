def gcd(a, b):
    if a < b:
        temp = a
        a = b
        b = temp
    while b != 0:
        q = a // b
        r = a % b
        a = b
        b = r
    return a

def extended_gcd(a, b):
    if a < b:
        temp = a
        a = b
        b = temp

    x0, y0 = 0, 1
    x1, y1 = 1, 0
    while b != 0:
        q = a // b
        r = a % b
        linearX = x0 - x1 * q
        linearY = y0 - y1 * q
        x0, y0 = x1, y1
        x1, y1 = linearX, linearY
        a, b = b, r
    return a, x0, y0

def mod_inverse(alpha, mod):
    gcd, x, y = extended_gcd(mod, alpha)
    if gcd != 1:
        print('No possible inverse')
        return -1
    else:
        return x % mod

def primitive_roots():
    p = int(input("Enter a prime number: "))
    g = set()
    for i in range(1, p):
        h = set()
        for j in range(1, p):
            h.add(pow(i, j, p))
        if len(h) == p - 1:
            g.add(i)
    print('\n', sorted(g), '\n')
