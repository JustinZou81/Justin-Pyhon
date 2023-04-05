import datetime

birthday = "1997-12-20"
birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d")
print(birthday_date, type(birthday_date))

curr_datetime = datetime.datetime.now()
print(curr_datetime, type(curr_datetime))

minus_datetime = curr_datetime-birthday_date
print(minus_datetime, type(minus_datetime))
print(minus_datetime.days/365)
