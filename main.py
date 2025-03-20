import holidays
print("Данный проект создан для определения празника в России по введеной в него дате")
ru_holidays = holidays.RU()
date_to_check = input("введите дату празника в формате гггг-мм-дд :  ")
holiday_name = ru_holidays.get(date_to_check)
if holiday_name:
    print(holiday_name)
else:
    print("на указаной вами дате празников нету")