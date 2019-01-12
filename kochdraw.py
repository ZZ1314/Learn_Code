# # kochdraw.py
#
# import turtle as t
#
#
# def koch(size, n):
#     if n == 0:
#         t.fd(size)
#     else:
#         for angle in [0, 60, -120, 60]:
#             t.left(angle)
#             koch(size / 3, n - 1)
#
#
# def main(size=400, level=3):
#     t.hideturtle()
#     t.speed(0)
#     t.setup(600, 600)
#     t.pu()
#     t.goto(-200, 100)
#     t.pd()
#     t.pensize(2)
#     for i in range(3):
#         koch(size, level)
#         t.right(120)
#     t.done()
#
#
