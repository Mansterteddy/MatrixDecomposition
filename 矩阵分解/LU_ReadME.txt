Author: Zhang Yuan
LUDecomposition.py is a program aiming at solving LU Decomposition of matrix, it can decompose a matrix into P, L and U matrix. The environment requires python3.0 and scipy, I import scipy to verify the correctness, if you have spicy, you can just recover 2,3,18-32,118 row to run the code. At last, you can input python Decomposition.py to use it in Terminal.

When you use it, you can input the matrix which will be decomposed in func load_data():

Input instance:

The matrix:
	1 4 5
	4 18 26
	3 16 30

The code you should change:    
	A=[[1,4,5],[4,18,26],[3,16,30]]

The result:
P:
[[0, 1, 0], [0, 0, 1], [1, 0, 0]]
L:
[[1.0, 0, 0], [0.75, 1.0, 0], [0.25, -0.2, 1.0]]
U:
[[4.0, 18.0, 26.0], [0, 2.5, 10.5], [0, 0, 0.6000000000000001]]

The complete result after recovery:
A:
array([[  1.,   4.,   5.],
       [  4.,  18.,  26.],
       [  3.,  16.,  30.]])
P:
array([[ 0.,  0.,  1.],
       [ 1.,  0.,  0.],
       [ 0.,  1.,  0.]])
L:
array([[ 1.  ,  0.  ,  0.  ],
       [ 0.75,  1.  ,  0.  ],
       [ 0.25, -0.2 ,  1.  ]])
U:
array([[  4. ,  18. ,  26. ],
       [  0. ,   2.5,  10.5],
       [  0. ,   0. ,   0.6]])
P:
[[0, 1, 0], [0, 0, 1], [1, 0, 0]]
L:
[[1.0, 0, 0], [0.75, 1.0, 0], [0.25, -0.20000000000000001, 1.0]]
U:
[[4.0, 18.0, 26.0], [0, 2.5, 10.5], [0, 0, 0.60000000000000009]]

The first P, L, U matrices are from scipy func.
The second P, L, U matrices are from my code.