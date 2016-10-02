def CountFactors(n): # count the number of factors other than 1 and n itself
    factors = []
    d = 2
    while d*d <= n:
        n2 = n
        while (n2 % d) == 0:
            factors.append(d)  # supposing you want multiple factors repeated
            n2 //= d
        d += 1
    return factors