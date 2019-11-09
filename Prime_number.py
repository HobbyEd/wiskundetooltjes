n = 100000
p = 2
while p <= n:
    is_prime = True
    for i in range(2, p):
        if p % i == 0:
            is_prime = False
            break
    if (is_prime is True):
        print(p)
    p = p + 1