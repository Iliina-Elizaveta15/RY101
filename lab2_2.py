salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.05  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

total_needed = 0
     # Запускаем расчеты по каждому месяцу
for month in range(months):
    # Если это первый месяц, то расходы остаются исходными
     if month == 0:
        current_spend = spend
else:
    # Увеличиваем расходы на 5% каждый последующий месяц
    current_spend *= (1 + increase)

    # Рассчитаем недостающую сумму
if current_spend > salary:
    deficit = current_spend - salary
    total_needed += deficit

money_capital =total_needed

print (f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", {money_capital})
