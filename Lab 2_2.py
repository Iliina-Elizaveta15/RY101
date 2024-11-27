salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.05  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
total_deficit = 0
current_spend = spend
def money_capital (salary, spend ):

    for month in range(10):
        deficit = max(0, current_spend - salary)
        total_deficit += deficit
        current_spend *= 1.05

print (f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", {money_capital})
