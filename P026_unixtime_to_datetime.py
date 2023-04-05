import datetime

unix_time = 1620747647
datetime_object = datetime.datetime.fromtimestamp(unix_time)
datetime_str = datetime_object.strftime("%Y-%m-%d %H-%M-%S")
print(datetime_str, type(datetime_str))
