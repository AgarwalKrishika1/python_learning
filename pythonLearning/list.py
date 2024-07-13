print("Empty list")
l=[]
print(l)

print("list")
l1=[1, 2, 'a', 3, 'b']
print(l1)
print("element at index 2")
print(l1[2])

print("multi dimentional list")
l2=[[1,2], [3,4]]
print(l2)
print("index 0,1")
print(l2[0][1])
print("index 1,1")
print(l2[1][1])
print("negative index")
print(l2[-2][-1])
print('length of list2')
print(len(l2))

print("take inputs")
String = input("enter list elements ")
List=  String.split()
print(List)

print("append l2")
l2.append('krishhu')
print(l2)
print("insert l1")
l1.insert(0,33)
print(l1)
print("extend list1")
l1.extend(['aaa', 7, 8])
print(l1)
print('reverse list')
l1.reverse()
print(l1)
l1.remove(33)
print(l1 ,'after remove')
#pop works with index numbers
l1.pop(4)
print(l1)

#slice list
print("list range 3-6")
slice_list = l1[3:6]
print(slice_list)
print('from index to end')
slice_list = l1[2:]
print(slice_list)
slice_list = l1[:-1]
print(slice_list, 'froom end ')

#expression and lists
print("expression and lists")
odd_square = [x ** 2 for x in range(1,11) if x%2==1]
print('square of odd number from 1 to 10', odd_square)