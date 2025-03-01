import datetime

x = datetime.datetime.now()

y = datetime.timedelta(days=1)

yesterday = x - y

tomorrow = x + y

print(yesterday)
print(tomorrow)

