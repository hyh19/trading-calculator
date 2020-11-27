# 交易总额
money = 200
print("交易总额", money)

# 交易次数
n = 10
print("交易次数", n)

# 每次交易金额
per_money = money / n
print("每次交易金额", per_money)

# 进场价格
base_price=100
print("进场价格", base_price)

# 交易间隔
interval = 0.01

print("----------")

for i in range(n):
    print("第 %d 次交易" % (i + 1))

    buy_price = base_price * (1 + interval * i)
    print("买入价格", buy_price)

    average_price = (base_price + buy_price) / 2
    print("平均成本", average_price)

    sum_money = per_money * (i + 1)
    print("仓位资金", sum_money)

    # 爆仓幅度
    bcfd = money / sum_money
    print("爆仓距离", bcfd)
    
    # 平均成本与爆仓价格的距离 平均成本 * (100 - 爆仓幅度) / 100
    zsjg = average_price * (100 - bcfd) / 100
    print("止损价格", zsjg)

    # 平均成本与爆仓价格的距离 当前价格 * (100 - 爆仓幅度) / 100
    ji = 1 - zsjg / buy_price
    print("当前价格距离爆仓价格距离", ji)
    print("----------")
