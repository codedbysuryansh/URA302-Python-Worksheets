import numpy as np

#Question1
a = np.arange(5, 26)
b = np.random.randint(10, 51, (3, 4))
print(a)
print(b)

#Question2
print(a.shape)
print(a.size)
print(a.dtype)

print(b.shape)
print(b.size)
print(b.dtype)

#Question3
arr1 = np.array([2,4,6,8,10])
arr2 = np.array([1,3,5,7,9])
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)

#Question4
c = np.arange(1,10).reshape(3,3)
print(c * 5)

#Question5
d = np.arange(10,26).reshape(4,4)
print(d[1])
print(d[:, -1])
d[0] = 0
print(d)

#Question6
e = np.random.randint(20, 41, 10)
print(e[e > 30])

#Question7
f = np.arange(11,23)
print(f.reshape(3,4))

#Question8
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(np.dot(A,B))
print(A.T)

#Question9
g = np.random.randint(10, 61, 15)
print(np.mean(g))
print(np.median(g))
print(np.std(g))

#Question10
M = np.array([[2,1,3],
              [0,5,6],
              [7,8,9]])
print(np.linalg.det(M))
print(np.linalg.inv(M))
print(np.linalg.eig(M))

#Question11
pos = np.array([[0,0],
                [2,3],
                [4,7],
                [7,10],
                [10,15]])

print(np.linalg.norm(pos[-1] - pos[0]))
print(np.sum(np.linalg.norm(np.diff(pos, axis=0), axis=1)))