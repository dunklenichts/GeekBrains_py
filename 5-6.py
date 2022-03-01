# 5. Запросите у пользователя значения выручки и издержек фирмы. 
#    Определите, с каким финансовым результатом работает фирма. 
#    Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. 
#    Выведите соответствующее сообщение.
# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки. 
#    Это отношение прибыли к выручке. 
#    Далее запросите численность сотрудников фирмы и определите прибыль фирмы 
#    в расчёте на одного сотрудника.

revenue = int(input('Enter your revenue: '))
costs = int(input('Enter your costs: '))
if (revenue > costs):
    print('You have proft. Congrdats.')
else:
    print('You have loss')
employee = int(input('Enter a number of employee: '))
profit = revenue - costs
profit_revenue = profit / revenue
print(f"Profitability of revenue is {profit_revenue:.2f}")
one_profit = profit_revenue / employee
print(f"Profitability of revenue per person is {one_profit:.2f}")

