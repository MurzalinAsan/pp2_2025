import math, time

def function(m, millisec):
    time.sleep(millisec/100)

    print(f"Square root of {m} after {millisec} miliseconds is {math.sqrt(m)}")

m = float(input())
millisec = int(input())
function(m, millisec)