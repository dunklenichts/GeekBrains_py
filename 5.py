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

