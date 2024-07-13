import numpy as np
arr = np.array([[1, 2, 3, 4, 4], [2, 3, 4, 5, 6]])
print(arr)

print("version")
print(np.__version__)
print('\n')

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)

print('check dimention of array')
print(arr.ndim)

print(arr[0, 1])
print('\n')
print('index of array')
arr = np.array([1, 2, 3, 4])
print(arr[1])
print('sum ', arr[0] + arr[1])

print('\n slicing')
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])

print('\n data type')
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

print('\n')
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('bool')
print(newarr)
print(newarr.dtype)

#if changes via copy it doesn't affect other
#if changes via view it does affect other

x = arr.copy()
x[0] = 21
print(x)
print(arr)
y = arr.view()
y[1] = 33
print(y)
print(arr)
#own data
print('\n')
print(x.base)
print(y.base)
print('shape ', arr.shape)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(3, 4)
print('reshape ', newarr)
newarr = arr.reshape(-1)
print('flatten', newarr)
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
for x in np.nditer(arr):
    print(x)
print('print with index')
for idx, x in np.ndenumerate(arr):
  print(idx, x)
arr = np.array([1, 2, 3, 4])
newarr = np.array([4, 5, 6, 7])

arr1 = np.concatenate((arr, newarr))
print('joined ',arr1)
print('join using stack')
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)
print('\n horizontal')
arr = np.hstack((arr1, arr2))
print(arr)
print('\n vertical')
arr = np.vstack((arr1, arr2))
print(arr)
print('\n depth')
arr = np.dstack((arr1, arr2))
print(arr)

print('\n split')
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)
print(newarr[0])

print('\n search')
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)

print('\n')
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

print('\n filter')
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

from numpy import random
#loc= mean  scale= standard deviation
x = random.normal(loc=1, scale=2, size=(2, 3))

print(x)