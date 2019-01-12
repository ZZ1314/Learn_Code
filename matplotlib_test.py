import matplotlib.pyplot as plt

# # matplotlib测试


# 设置坐标点
x = list(range(1, 1001))
y = [i ** 2 for i in x]
plt.scatter(x, y, c=y, cmap=plt.cm.Blues, edgecolors="none", s=10)
# 设置线段宽度
# plt.plot(input_value, squares, linewidth=0.5)
# # 设置标题 标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Values", fontsize=14)
# # 设置刻度属性
# plt.tick_params(axis="both", labelsize=14)
# x,y坐标轴取值范围
plt.axis([0, 1100, 0, 1100000])
plt.tick_params(axis="both", which="major", labelsize=14)

plt.show()
