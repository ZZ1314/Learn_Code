# pi = 0
# n = 1000
# for i in range(n):
#     pi += 1 / pow(16, i) * (
#             4 / (8 * i + 1) - 2 / (8 * i + 4) -
#             1 / (8 * i + 5) - 1 / (8 * i + 6))
#
# print("{}".format(pi))

from random import random
from time import perf_counter

darts = 10000 * 10000
hits = 0
start = perf_counter()
for i in range(1, darts + 1):
    x, y = random(), random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1:
        hits += 1
pi = 4 * (hits / darts)
print("{}".format(pi))
print("{}".format(perf_counter() - start))
