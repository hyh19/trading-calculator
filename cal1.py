from decimal import *

getcontext().prec = 7

total_money = Decimal(200)
print("交易总额", total_money)

n = 4
print("交易次数", n)

unit_money = Decimal(total_money) / Decimal(n)
print("单位金额", unit_money)

base_price = Decimal(100)
print("进场价格", base_price)

interval = Decimal("0.01")
print("交易间隔 {:.2f}%".format(Decimal(interval) * Decimal(100)))

print("-" * 36)

for i in range(n):

    print("第 {} 次交易".format(i + 1))

    buy_price = Decimal(base_price) * (Decimal(1) +
                                       Decimal(interval) * Decimal(i))
    print("买入价格 {:.2f}".format(buy_price))

    average_price = (Decimal(base_price) + Decimal(buy_price)) / Decimal(2)
    print("持仓均价 {:.2f}".format(average_price))

    position_money = Decimal(unit_money) * Decimal(i + 1)
    print("仓位资金 {:.2f}".format(position_money))

    average_price_blow_up_points = Decimal(total_money) / Decimal(position_money)
    print("持仓均价爆仓点数 {:.2f}%".format(average_price_blow_up_points))

    # 爆仓价格
    # 计算公式：持仓均价 * (1 - 爆仓点数 / 100)
    blow_up_price = Decimal(average_price) * (1 - (Decimal(average_price_blow_up_points) / Decimal(100)))
    print("爆仓价格 {:.2f}".format(blow_up_price))
    
    # 计算公式：1 - 爆仓价格 / 买入价格
    buy_price_blow_up_points = (Decimal(1) - Decimal(blow_up_price) / Decimal(buy_price)) * Decimal(100)
    print("买入价格爆仓点数 {:.2f}%".format(buy_price_blow_up_points))
    print("-" * 36)
