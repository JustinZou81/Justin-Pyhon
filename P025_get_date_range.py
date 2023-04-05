import datetime


def get_date_range(begin_date, end_date):
    date_list = []
    while begin_date <= end_date:
        date_list.append(begin_date)
        begin_date_object = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
        days1_timedelta = datetime.timedelta(days=1)
        begin_date = (begin_date_object+days1_timedelta).strftime("%Y-%m-%d")
    return date_list


begin_date = "2021-04-28"
end_date = "2021-05-03"
date_list = get_date_range(begin_date, end_date)
print(date_list)
