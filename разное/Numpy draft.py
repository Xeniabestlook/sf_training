import numpy as np
a = np.int8(25)

print(np.iinfo(np.uint64))

print(np.uint8(-456))

arr = np.array([1,2,3,4,5], dtype=np.int8)
print(arr)

print(type(arr))

nd_arr = np.array([
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
])

print(nd_arr)

print(arr.dtype)

arr = np.array([345234, 876362.12, 0, -1000, 99999999])

arr = np.float64(arr)

print(arr)

arr, step = np.linspace(-6, 21, 60, retstep=True, endpoint=False)
print(round(step, 2))

arr = np.arange(8)
arr.shape = (2,4)
print(arr)

arr1 = np.arange(8)
arr1_new = arr1.reshape(2,4, order='F')

print(arr1)
print(arr1_new)

arr1_trans = arr1_new.transpose()

print(arr1_trans)
print()
arr = np.linspace(1, 2, 12).reshape(3,4)
print(arr)
rev = arr[1, ::-1]
print('rev')
print(rev)


print(np.iinfo(np.int16))