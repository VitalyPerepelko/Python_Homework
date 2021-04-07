#Task1 

print("Промежуток времени в зависимости от его продолжительности: ")
duration = int(input())
second_in_minute = 60
second_in_hour = second_in_minute * 60
second_in_day = second_in_hour * 24
second_in_week = second_in_day * 7
second_in_month = second_in_week * 4
second_in_year = second_in_month * 12


day = duration // second_in_day
hour = (duration - (day * second_in_day)) // second_in_hour
minute = (duration - (day * second_in_day) - (hour * second_in_hour)) // second_in_minute
second = (duration - (day * second_in_day) - (hour * second_in_hour)) % second_in_minute

if day > 0:
    day = str(day) + " дней"
else:
    day = ""

if hour > 0:
    hour = str(hour) + " часов"
else:
    hour = ""

if minute > 0:
    minute = str(minute) + " минут"
else:
    minute = ""

if second > 0:
    second = str(second) + " секунд"
else:
    second = ""
print(day, hour, minute, second)

#Task2

my_list = []
for num in range(1, 1001, 2):
    my_list.append(num ** 3)

final_sum = 0
for num in my_list:
    check_sum = 0
    for check_num in str(num):
        check_sum += int(check_num)
    if check_sum % 7 == 0:
        final_sum += num
print(final_sum)

final_sum = 0
for num in my_list:
    num += 17
    check_sum = 0
    for check_num in str(num):
        check_sum += int(check_num)
    if check_sum % 7 == 0:
        final_sum += num
print(final_sum)

#task 3

percent = int(input('Введите число процента: '))
if percent == 1:
   word = "процент"
elif percent <= 4:
    word = "процента"
else:
    word = "процентов"
print(percent, word)