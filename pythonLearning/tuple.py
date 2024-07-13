t1 = ()
print('empty tuple', t1)
t1=[1,2,3]
print('list in tuple', tuple(t1))
t1='Krishu'
print('string to tuple', tuple(t1))
t1= ('a',)*3
print('repetation', t1)
print('tuple using loop')
n=5
for i in range(int(n)):
    t1= t1+ tuple(('a'))
    print(t1)
#delete tuple
#del (t1)
#print(t1)
t1=(1,2,3,4,5,6,7,8,9,0)
print('min',min(t1))
print('max',max(t1))
print('sum',sum(t1))
print('sorted',sorted(t1))
print('length',len(t1))