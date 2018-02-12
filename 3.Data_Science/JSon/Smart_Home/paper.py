import datetime

k = datetime.datetime.now()
print(k)

base_date = str(k.year) + "{0:0>2}".format(str(k.month))
base_time = "{0:0>2}".format(str(k.hour)) + "{0:0>2}".format(str(k.minute))

print(base_date)
print(base_time)