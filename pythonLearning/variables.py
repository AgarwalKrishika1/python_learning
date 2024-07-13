#variables

x=1
print(f'{x} is  of type of {type(x).__name__}')
x="hiii"
print(f'{x} is  of type of {type(x).__name__}')
x=2.11123
print(f'{x} is  of type of {type(x).__name__}')
x=[1, 2, 3]
print(f'{x} is  of type of {type(x).__name__}')

y=x
print(y)
x.append(8)
#change in x changes y
print(x)
print(y)
 #variable with equals doesnt change  values of assigned previous
x= 'add'
print(y)
print(x)

