salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0  # Подушка безопасности

for _ in range(months):
    delta_salary_and_spend = spend - salary  # Определяем сколько нужно положить в подушку безопасности

    money_capital += delta_salary_and_spend  # Увеличиваем размер подушки безопасности
    spend *= increase + 1  # Увеличиваем траты

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital, 2))
