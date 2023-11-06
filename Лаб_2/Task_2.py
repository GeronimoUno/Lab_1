salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
difference = spend - salary
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for i in range(2,months + 1):
    spend *= increase + 1
    difference += spend - salary
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(difference, 2))
