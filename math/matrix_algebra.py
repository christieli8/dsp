# Matrix Algebra

import numpy as np

A = np.matrix([[1, 2, 3], [2, 7, 4]])
B = np.matrix([[1, -1], [0, 1]])
C = np.matrix([[5, -1], [9, 1], [6, 0]])
D = np.matrix([[3, -2, -1], [1, 2, 3]])

u = np.matrix([6, 2, -3, 5])
v = np.matrix([3, 5, -1, 4])
w = np.matrix([[1], [8], [0], [5]])

# 1
```(2, 3)
(2, 2)
(3, 2)
(2, 3)
(1, 4)
(1, 4)
(4, 1)
```
print A.shape
print B.shape
print C.shape
print D.shape
print u.shape
print v.shape
print w.shape

# 2
```
[[ 9  7 -4  9]]
[[ 3 -3 -2  1]]
[[ 36  12 -18  30]]
[[51]]
8.60232526704
```

print u + v

print u - v

a = 6
print 6*u

print u.dot(v.T)

print np.linalg.norm(u)

# 3
```
[[14  3  3]
 [ 2  7  9]]
[[-1 -5 -1]
 [ 2  7  4]]
```
print A + C

print A - C.T

print C.T + 3*D

print B * A

print B * A.T

print B * C

print C * B

print B^4

print A * A.T

print D.T * D
