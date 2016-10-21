# -*- coding: utf-8 -*-
# Draw circle at (0, 0) with radius r. How many points with integer coordinates will fall into the circle? 
# If r = 1, then point (0, 0), (1, 0), (0, 1), (0, -1), (-1, 0) will. Return 5. 输入限制 r is [0, 20000].
# for n between 0 and 12, we should get 1, 5, 13, 29, 49, 81, 113, 149, 197, 253, 317, 377, 441
# https://en.wikipedia.org/wiki/Gauss_circle_problem
def LatticePoints(n):
    bound = int(n)
    count = 0
    for i in range(-bound, bound+1):
        for j in range(-bound, bound+1):
            if (i**2 + j**2) <= n**2:
                #print i, j
                count += 1

    return count