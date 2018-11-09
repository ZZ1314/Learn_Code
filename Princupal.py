def invest(amount, rate, time):
    while time > 0:
        amount = amount * (1 + rate/100)
        time -= 1
        print(int(amount))


invest(rate=6, time=10, amount=10000000)
