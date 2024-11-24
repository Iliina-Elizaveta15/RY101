money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

months = 0
current_capital = money_capital
current_spend = spend

while True:
    budget = current_capital + salary
    if budget >= current_spend:
        months += 1
        current_capital = budget - current_spend
        current_spend *= 1.05  # Увеличиваем расходы на 5%
    else:
        break


print("Количество месяцев, которое можно протянуть без долгов:", months)
