import pprint
#import scipy
#import scipy.linalg #Scipy Linear Algebra Library


def load_data():
    A=[[1,4,5],[4,18,26],[3,16,30]]
    flag=True
    #A=scipy.array([[1,4,5],[4,18,26],[3,16,30]])
    B=[]
    for a in range(len(A)):
        B1=[]
        if len(A[a])!=len(A):
            flag=False
        for b in range(len(A[a])):
            B1.append(float(A[a][b]))
        B.append(B1)
    if flag==False:
        B=0
            #B=scipy.array(B)
    return B

'''
def Scipy_LU(A):
  A=scipy.array(A)
  P,L,U=scipy.linalg.lu(A)

  print "A:"
  pprint.pprint(A)

  print "P:"
  pprint.pprint(P)

  print "L:"
  pprint.pprint(L)

  print "U:"
  pprint.pprint(U)
'''

def multiply_matrix(M,N):
    """Multiply square matrices of same dimension M and N"""
    List_N=zip(*N)

    return [[sum(el_m*el_n for el_m, el_n in zip(row_m,col_n)) for col_n in List_N] for row_m in M]

def partial(A,flag,cur):
    for i in range(cur,len(A)):
        if i==cur:
            pos_index=cur
            pos=A[cur][cur]
        elif abs(A[i][cur])>abs(pos):
            pos_index=i
            pos=A[i][cur]
        else:
            pass

    for i in range(len(A[cur])):
        A[cur][i], A[pos_index][i]=A[pos_index][i], A[cur][i]

    flag[cur],flag[pos_index]=flag[pos_index],flag[cur]

    return A,flag

def LU_Decomposition(A):
    row=len(A)
    col=len(A[0])
    flag=[]
    for i in range(len(A)):
        flag.append(i+1)
    for i in range(row):
        A,flag=partial(A,flag,i)
        divider_down=A[i][i]
        for j in range(i,row-1):
            divider=float(A[j+1][i])/divider_down
            for k in range(i,col):
                if k==i:
                    A[j+1][k]=divider
                else:
                    A[j+1][k]-=A[i][k]*divider
    return A, flag


def Print_Matrix(A,flag):
    Flag_Len=len(flag)
    P=[]
    for i in range(Flag_Len):
        P_son=[]
        for j in range(Flag_Len):
            if j == flag[i]-1:
                P_son.append(1)
            else:
                P_son.append(0)
        P.append(P_son)
    print "P:"
    pprint.pprint(P)

    L=[]
    U=[]
    Matrix_Len=len(A)
    for i in range(Matrix_Len):
        L_son=[]
        U_son=[]
        for j in range(Matrix_Len):
            if i>j:
                L_son.append(A[i][j])
                U_son.append(0)
            elif i==j:
                L_son.append(1.0)
                U_son.append(A[i][j])
            else:
                L_son.append(0)
                U_son.append(A[i][j])
        L.append(L_son)
        U.append(U_son)

    print "L:"
    pprint.pprint(L)
    print "U:"
    pprint.pprint(U)

if __name__ == "__main__":
    A=load_data()
    if A==0:
        print "Wrong Matrix!"
    #Scipy_LU(A)
    else:
        A,flag=LU_Decomposition(A)
        Print_Matrix(A,flag)

