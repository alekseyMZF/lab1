money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
budget = money_capital + salary

month = 0
while True:
    difference = spend - salary
    if difference > money_capital:
        break
    spend += spend * increase
    money_capital -= difference
    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)
print(f'Количество оставшихся денег под конец безбедного периода: {money_capital % difference:.2f}')
