#operaots

#add sub mul
x= (2+3)*(3.0-1)
print(x)
#div
print('true division : ', 11/2)
print('floor division:', 11//2)

print("modulus:", 11%2)
print('exponentiatial', 11**2)
#comaprison

print('25 odd', 25%2==1)
print('20 odd',20%2==1)

x=10
print('x in between ',6<x<15)

#date time
from _datetime import datetime,date,time
dt = datetime(2023, 6, 6, 11,47,30)
print('day:' , dt.day)
print("minutes:", dt.minute)
print(dt.strftime('%m/%d/%Y %H:%M'))