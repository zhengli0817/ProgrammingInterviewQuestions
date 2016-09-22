# for n between 0 and 12, we should get 1, 5, 13, 29, 49, 81, 113, 149, 197, 253, 317, 377, 441
# https://en.wikipedia.org/wiki/Gauss_circle_problem
def LatticePoints(n):
    bound = int(n)+2
    count = 0
    for i in range(-bound, bound):
        for j in range(-bound, bound):
            if (i**2 + j**2) <= n**2:
                count += 1

    return count