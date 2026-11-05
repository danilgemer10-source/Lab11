import csv

days = []
temperatures = []

with open("D:/дз/ВКН/lab11 full/lab11/temperatures.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        day = int(row[0])
        temperature = int(row[1])

        days.append(day)
        temperatures.append(temperature)

        print('День:', day, 'Температура:', temperature)

min_temp = min(temperatures)

print("Найнижча температура:", min_temp)

print("Була такого числа:")
for i in range(len(temperatures)):
    if temperatures[i] == min_temp:
        print(days[i])

max_temp = max(temperatures)

print("Найвища температура:", max_temp)

print("Була такого числа:")
for i in range(len(temperatures)):
    if temperatures[i] == max_temp:
        print(days[i])
