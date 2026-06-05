# dtype is used to find the type of array in int float etc
import numpy as np 
 
arr_1d = np.array([1,2,3])
print(arr_1d.dtype)
arr_1d = np.array([1,2 + 1j,3])
print(arr_1d.dtype)
arr_1d = np.array([1,2.7,3])
print(arr_1d.dtype)
arr_1d = np.array([1,True,3])
print(arr_1d.dtype)
