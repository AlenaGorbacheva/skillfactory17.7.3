deposit = []
per_cent = {'ТБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28,'СБЕР': 4.0}
money = int(input ('Введите сумму вклада'))
deposit.append (per_cent['ТБ'] * money/100)
deposit.append (per_cent['СКБ'] * money/100)
deposit.append (per_cent['ВТБ'] * money/100)
deposit.append (per_cent['СБЕР'] * money /100)
deposit = (5600, 5900, 4280, 4000)
print ( "годовой процент=", deposit)
print ( "Максимальная сумма, которую вы можете заработать=", max(deposit))
