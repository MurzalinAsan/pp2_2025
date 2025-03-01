import datetime

date1 = datetime.datetime(2025, 5, 2, 2, 6, 34)
date2 = datetime.datetime(2025, 5, 2, 2, 6, 27)
dif = (date1 - date2).total_seconds()

print(dif)