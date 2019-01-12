# 反向排序
# def rvs(s):
#     if s == "":
#         return s
#     else:
#         return rvs(s[1:]) + s[0]

# 斐波那契
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)


# 汉诺塔
count = 0


def hanoi(n, src="A", dst="C", mid="B"):
    global count
    if n == 1:
        print("{}:{}->{}".format(1, src, dst))
        count += 1
    else:
        hanoi(n - 1, src, mid, dst)
        print("{}:{}->{}".format(n, src, dst))
        count += 1
        hanoi(n - 1, mid, dst, src)


hanoi(2)