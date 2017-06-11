Author: Zhang Yuan

This file aims at explaining all details about the program Decomposition. decomposition.py is a program aiming at solving matrix decomposition, it includes LU decomposition, QR decomposition, Householder decomposition and Givens decomposition. The environment requires python2.6 and above, without any package, I rewrite all matrix operation which is necessary. You should input python decomposition.py to use it in Terminal.

When you use it, you can input the matrix which will be decomposed in main function:

Input instance:

The matrix:
	1  4  5
	4 18 26	
	3 16 30
	1  4  5

The code you should change in row 647:
    Matrix=[[1,4,5],[4,18,26],[3,16,30],[1,4,5]]

And you can choose the algorithm you want to decompose the matrix:

I implement PA=LU in LU decomposition, but this method is not suitable for singular matrix.

I implement QR decomposition(Gram-Schmidt), but in modified way which makes calculation more suitable.

I implement Householder decomposition, not only for square matrix, but also for rectangle matrix.

I implement Givens decomposition, not only for square matrix, but also for rectangle matrix.

An instance shows below:

```
The matrix:

    1  4  5
    4 18 26	
    3 16 30
    1  4  5

1.LU decomposition

2.QR decomposition

3.Householder decomposition

4.Givens Decomposition

0.Exit1

Wrong Matrix!

1.LU decomposition

2.QR decomposition

3.Householder decomposition

4.Givens Decomposition

0.Exit2

Q:

[[0.19245008972987526, -0.32530002431617755, 0.597614304667195],

 [0.769800358919501, -0.42289003161103056, -0.47809144373376233],

 [0.5773502691896257, 0.7807200583588269, 0.23904572186687775],

 [0.19245008972987526, -0.32530002431617755, 0.597614304667195]]

R:

[[5.196152422706631, 24.63361148542403, 39.25981830489455],

 [3.4416913763379853e-15, 2.277100170213259, 9.173460685716234],

 [-2.5979218776228663e-14, -1.1812772982011666e-13, 0.7171371656004624]]

A:

[[0.9999999999999832, 3.999999999999925, 4.999999999999889],

 [4.000000000000011, 18.00000000000005, 26.000000000000075],

 [2.999999999999996, 15.999999999999982, 29.999999999999975],

 [0.9999999999999832, 3.999999999999925, 4.999999999999889]]

1.LU decomposition

2.QR decomposition

3.Householder decomposition

4.Givens Decomposition

0.Exit3

Q:

[[-0.19245008972987532,

  0.32530002431617777,

  -0.597614304667198,

  -0.7071067811865464],

 [-0.769800358919501,

  0.42289003161103117,

  0.47809144373375734,

  -8.326672684688674e-16],

 [-0.5773502691896257,

  -0.7807200583588266,

  -0.23904572186687864,

  2.983724378680108e-16],

 [-0.19245008972987526,

  0.32530002431617755,

  -0.5976143046671955,

  0.7071067811865488]]

R:

[[-5.196152422706631, -24.633611485424034, -39.25981830489456],

 [1.1102230246251565e-16, -2.277100170213243, -9.173460685716213],

 [0.0, 0.0, -0.7171371656006369],

 [0.0, -4.440892098500626e-16, -4.440892098500626e-16]]

A:

[[1.0000000000000002, 4.000000000000002, 5.0000000000000036],

 [3.9999999999999996, 18.000000000000004, 26.000000000000007],

 [2.9999999999999996, 15.999999999999998, 30.000000000000004],

 [0.9999999999999999, 4.000000000000002, 5.000000000000003]]

1.LU decomposition

2.QR decomposition

3.Householder decomposition

4.Givens Decomposition

0.Exit4

Q:

[[0.19245008972987526,

  -0.32530002431617777,

  0.5976143046671976,

  -0.7071067811865469],

 [0.769800358919501,

  -0.42289003161103106,

  -0.47809144373375745,

  -4.163336342344337e-16],

 [0.5773502691896257,

  0.7807200583588267,

  0.23904572186687872,

  1.6653345369377348e-16],

 [0.1924500897298752,

  -0.32530002431617755,

  0.597614304667196,

  0.7071067811865481]]

R:

[[5.196152422706632, 24.633611485424037, 39.25981830489456],

 [-3.6803534893647714e-17, 2.277100170213245, 9.173460685716213],

 [6.761241091511459e-17, 0.0, 0.7171371656006367],

 [8.000008346030682e-17, 0.0, 0.0]]

A

[[0.9999999999999999, 4.0, 5.000000000000002],

 [4.0, 18.000000000000004, 26.000000000000007],

 [3.0, 16.000000000000004, 30.000000000000004],

 [0.9999999999999999, 4.0, 5.000000000000001]]

1.LU decomposition

2.QR decomposition

3.Householder decomposition

4.Givens Decomposition

0.Exit0

End!

```

At first decomposition, when you input 1, LU decomposition is not suitable singular matrix, so it outputs wrong matrix. 

Secondly, when you input 2, QR decomposition outputs an orthogonality matrix Q, an upper-triangle matrix R, the A is the product of Q and R, try to verify the correctness.

Thirdly, when you input 3, Householder decomposition outputs an orthogonality matrix Q, an upper-triangle matrix R, the A is the product of Q and R, try to verify the correctness.

Finally, when you input 4,Givens decomposition outputs an orthogonality matrix Q, an upper-triangle matrix R, the A is the product of Q and R, try to verify the correctness.

When you input 0, you exit the program.

