from decimal import *

getcontext().prec = 6

money = Decimal(300)
print("交易总额", money)

n = 6
print("交易次数", n)

per_money = Decimal(money) / Decimal(n)
print("每次交易金额", per_money)

base_price = Decimal(18000)
print("进场价格", base_price)

interval = Decimal("0.01")
print("交易间隔", interval)

print("----------")

for i in range(n):
    print("第 %d 次交易" % (i + 1))

    buy_price = Decimal(base_price) * ( Decimal(1) + Decimal(interval) * Decimal(i) )
    print("买入价格", buy_price)

    average_price = ( Decimal(base_price) + Decimal(buy_price) ) / Decimal(2)
    print("平均价格", average_price)

    sum_money = Decimal(per_money) * Decimal(i + 1)
    print("仓位资金", sum_money)

    baocang_distance = Decimal(money) / Decimal(sum_money)
    print("平均价格与爆仓价格距离（百分比）", baocang_distance)
    
    # 平均成本与爆仓价格的距离 
    # 计算公式：平均成本 * (100 - 爆仓幅度) / 100
    baocang_price = Decimal(average_price) * ( Decimal(100) - Decimal(baocang_distance) ) / Decimal(100)
    print("爆仓价格", baocang_price)

    # 计算公式：当前价格 * (100 - 爆仓幅度) / 100
    current_price_distance = Decimal(1) - Decimal(baocang_price) / Decimal(buy_price)
    print("当前价格与爆仓价格距离（百分比）", Decimal(current_price_distance) * Decimal(100))
    print("----------")
