money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

count_months = 0  # Количество месяцев без долгов

while True:
    budget = money_capital + salary  # Бюджет текущего месяца

    balance_after_spending = budget - spend  # Остаток от бюджета после трат
    if balance_after_spending <= 0:
        break

    count_months += 1

    delta_salary_and_spend = spend - salary  # Считаем сколько денег взяли из подушки безопасности в текущем месяце
    money_capital -= delta_salary_and_spend  # Считаем сколько осталось в подушке безопасности

    spend *= increase + 1  # Считаем увеличившиеся затраты

print("Количество месяцев, которое можно протянуть без долгов:", count_months)
