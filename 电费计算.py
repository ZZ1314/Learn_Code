May = 6745.94
Jun = 6716.46
Jul = 6969.83
Aug = 7687.73
Sep = 7328.50
Oct = 7388.73
Basic_electricity = 5355 * 4
electricity_1 = 31 * 80
electricity_2 = 68.3 * 60 - electricity_1
total = Jul + Jun + Aug + Sep

print("双方5-10月用电费用总计：" + str(total))

print(
    "容量电费总计:" + str(Basic_electricity) + ",天津中科先进技术研究院承担:" + str(Basic_electricity / 3) + ",天津中科宇航联创承担:" + str(
        Basic_electricity / 3 * 2))

print("使用电费总计:" + str(round(total - Basic_electricity, 2)))

print(
    "天津中科先进技术研究院读表：" + str(electricity_2) + "度,支付电费：" + str(
        round((total - Basic_electricity) / (electricity_2 + electricity_1) * electricity_2, 2)))

print("天津中科宇航联创读表：" + str(electricity_1) + "度,支付电费：" + str(
    round((total - Basic_electricity) / (electricity_2 + electricity_1) * electricity_1, 2)))
