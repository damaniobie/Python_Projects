import numpy as np
import time
import sys

a = np.array([1,2,3])

#list and numpy array are quite similar, but numpy array is far more convenient and faster
l = range(1000)
print(sys.getsizeof(5)*len(l))

array = np.arange(1000)
print(array.size*array.itemsize)

print("\n\n")

size = 10000000

l1 = range(size)
l2 = range(size)

a1 = np.arange(size)
a2 = np.arange(size)

start = time.time()
time_eq = (time.time()-start)*1000
result = [(x+y) for x,y in zip(l1,l2)]

print("list took: ", time_eq)
result = a1 + a2
print("numpy took: ",time_eq)

#multiplying lists
print("\n\n")
list_a = np.array([54.3,78.4,92.2,20.4])
list_b = np.array([77.3,44.7,86.2,100.4])

print(list_a * list_b)
