#coding=utf-8
import pprint
import math

class LU:
    
    @staticmethod
    def load_data(A):
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

    @staticmethod
    def multiply_matrix(M,N):
        """Multiply square matrices of same dimension M and N"""
        List_N=zip(*N)
        return [[sum(el_m*el_n for el_m, el_n in zip(row_m,col_n)) for col_n in List_N] for row_m in M]

    @staticmethod
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

    @staticmethod
    def LU_Decomposition(A):
        row=len(A)
        col=len(A[0])
        flag=[]
        for i in range(len(A)):
            flag.append(i+1)
        for i in range(row):
            A,flag=LU.partial(A,flag,i)
            divider_down=A[i][i]
            for j in range(i,row-1):
                divider=float(A[j+1][i])/divider_down
                for k in range(i,col):
                    if k==i:
                        A[j+1][k]=divider
                    else:
                        A[j+1][k]-=A[i][k]*divider
        return A, flag


    @staticmethod
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

    @staticmethod
    def solve(matrix):
        A=LU.load_data(matrix)
        if A==0:
            print "Wrong Matrix!"
        else:
            A,flag=LU.LU_Decomposition(A)
            LU.Print_Matrix(A,flag)

class QR:
    #Handle vector w and vector v's Inner product
    @staticmethod
    def InnerProduct(w,v):
        sum=0
        for i in range(len(w)):
            sum+=w[i]*v[i]
    
        return sum

    @staticmethod
    #将matrix行列翻转，用于矩阵乘法
    def handleMatrix(matrix):
        mat=[]
        for i in range(len(matrix[0])):
            mat_son=[]
            for j in range(len(matrix)):
                mat_son.append(matrix[j][i])
            mat.append(mat_son)
        return mat

    @staticmethod
    #用于处理vector的减法
    def minus(in_1,in_2):
        temp=[]
        for i in range(len(in_1)):
            temp_son=in_1[i]-in_2[i]
            temp.append(temp_son)
        return temp

    @staticmethod
    #用于处理常数和vector的乘法
    def multiply(a,list_b):
        for i in range(len(list_b)):
            list_b[i]=list_b[i]*a
        return list_b

    @staticmethod
    #用于处理两个vector的乘法，相当于Inner Product
    def multiply_list(list_a,list_b):
        list=0
        for i in range(len(list_a)):
            list+=list_a[i]*list_b[i]
        return list
 
    @staticmethod
    #用于处理两个矩阵的乘法
    def multiply_matrix(matrix_a,matrix_b):
        matrix=[]
        matrix_b=QR.handleMatrix(matrix_b)
        for i in range(len(matrix_a)):
            matrix_son=[]
            for j in range(len(matrix_b)):
                matrix_son.append(QR.multiply_list(matrix_a[i],matrix_b[j]))
            matrix.append(matrix_son)
        return matrix

    @staticmethod
    #QR分解核心代码
    #本质就是Gram Method
    def QR_decomposition(matrix):
        source=matrix
        matrix=QR.handleMatrix(matrix)
        u=[]
        u.append(matrix[0])
        #处理出正交基底中的每一个正交向量
        for i in range(1,len(matrix)):
            for j in range(i,len(matrix)):
                matrix[j]=QR.minus(matrix[j],QR.multiply(float(QR.InnerProduct(matrix[j],u[i-1]))/QR.InnerProduct(u[i-1],u[i-1]),u[i-1]))
            u.append(matrix[i])
        #单位化正交向量
        for i in range(len(u)):
            u[i]=QR.multiply(math.sqrt(1.0/QR.InnerProduct(u[i],u[i])),u[i])
        #计算R矩阵，使用Q的转置乘以原矩阵
        R=QR.multiply_matrix(u,source)
        return u,R


    @staticmethod
    def solve(matrix):
        Q,R=QR.QR_decomposition(matrix)
        print "Q:"
        pprint.pprint(QR.handleMatrix(Q))
        print "R:"
        pprint.pprint(R)
        print "A:"
        pprint.pprint(QR.multiply_matrix(QR.handleMatrix(Q),R))

class Householder:
    @staticmethod
    #两个vector的内积
    def InnerProduct(w,v):
        sum=0
        for i in range(len(w)):
            sum+=w[i]*v[i]
        return sum

    @staticmethod
    #处理vector，使之成为vector的转置
    def handleList(list):
        li=[]
        for i in range(len(list)):
            list_son=[]
            list_son.append(list[i])
            li.append(list_son)
        return li

    @staticmethod
    #处理matrix，行列互换，成为矩阵的转置
    def handleMatrix(matrix):
        mat=[]
        for i in range(len(matrix[0])):
            mat_son=[]
            for j in range(len(matrix)):
                mat_son.append(matrix[j][i])
            mat.append(mat_son)
        return mat

    @staticmethod
    #两个向量的加法
    def add(in_1,in_2):
        temp=[]
        for i in range(len(in_1)):
            temp_son=in_1[i]+in_2[i]
            temp.append(temp_son)
        return temp

    @staticmethod
    #两个向量的减法
    def minus(in_1,in_2):
        temp=[]
        for i in range(len(in_1)):
            temp_son=in_1[i]-in_2[i]
            temp.append(temp_son)
        return temp

    @staticmethod
    #两个矩阵的减法
    def minus_mat(in_1,in_2):
        temp=in_1
        for i in range(len(in_1)):
            for j in range(len(in_1[0])):
                temp[i][j]-=in_2[i][j]
        return temp

    @staticmethod
    #两个向量的加法
    def add(in_1,in_2):
        temp=[]
        for i in range(len(in_1)):
            temp_son=in_1[i]+in_2[i]
            temp.append(temp_son)
        return temp

    @staticmethod
    #常数和向量的乘法
    def multiply(a,list_b):
        for i in range(len(list_b)):
            list_b[i]=list_b[i]*a
        return list_b

    @staticmethod
    #常数和矩阵的乘法
    def multiply_mat(a,matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j]=a*matrix[i][j]
        return matrix

    @staticmethod
    #两个向量的乘法得到一个数，相当于两个向量的内积
    def multiply_list(list_a,list_b):
        list=0
        for i in range(len(list_a)):
            list+=list_a[i]*list_b[i]
        return list

    @staticmethod
    #两个向量相乘得到一个矩阵
    def multiply_list_matrix(list_a,list_b):
        mat=[]
        for i in range(len(list_a)):
            matrix_son=[]
            for j in range(len(list_b)):
                matrix_son.append(list_a[i][0]*list_b[j])
            mat.append(matrix_son)
        return mat

    @staticmethod
    #两个矩阵相乘
    def multiply_matrix(matrix_a,matrix_b):
        matrix=[]
        matrix_b=Householder.handleMatrix(matrix_b)
        for i in range(len(matrix_a)):
            matrix_son=[]
            for j in range(len(matrix_b)):
                matrix_son.append(Householder.multiply_list(matrix_a[i],matrix_b[j]))
            matrix.append(matrix_son)
        #print matrix
        return matrix

    @staticmethod
    #构造一个n*n的单位矩阵
    def construct(n):
        I=[]
        for i in range(n):
            I_son=[]
            for j in range(n):
                if i==j:
                    I_son.append(1)
                else:
                    I_son.append(0)
            I.append(I_son)
        return I

    @staticmethod

    def Householder_1(matrix):
        m=len(matrix)
        n=len(matrix[0])
        R=matrix
        Q=[]
        R_result=[]
        Q_result=[]
        matrix_temp=[]
        for i in range(m):
            matrix_temp_son=[]
            for j in range(n):
                matrix_temp_son.append(matrix[i][j])
            matrix_temp.append(matrix_temp_son)
        #print "matirx_temp",matrix_temp
        #创建Q_result和R_result
        for i in range(m):
            Q_result_son=[]
            for j in range(m):
                if i==j:
                    Q_result_son.append(1)
                else:
                    Q_result_son.append(0)
            Q_result.append(Q_result_son)
    
        for i in range(m):
            R_result_son=[]
            for j in range(n):
                if i==j:
                    R_result_son.append(1)
                else:
                    R_result_son.append(0)
            R_result.append(R_result_son)

        #Householder不断循环，R矩阵从n*n、n-1*n-1、...、1*1，而Q矩阵每次循环决定一个，最终Q由所有Q矩阵相乘得到
        #另外最终的Q矩阵的逆就是相乘Q矩阵的转置，可以根据正交矩阵的定义得到。所以我们最后得到的Q矩阵乘以原矩阵，就可以得到R矩阵，要想得到QR，只需将Q矩阵转置。
        for i in range(n):
            #每次选取的正交向量长度从n变到1
            x=[]
            for j in range(i,m):
                x.append(matrix[j][i])
            #如果无法继续下去，就停止，这是针对m<n的情况
            if len(x)==0:
                break
            e=[]
        #选择单位向量
            for k in range(len(x)):
                e.append(0)
            e[0]=1
        #计算得到u
            u=Householder.multiply(math.sqrt(Householder.InnerProduct(x,x)),e)
            u=Householder.add(x,u)
            u_T=Householder.handleList(u)
            mat=Householder.multiply_list_matrix(u_T,u)
        #print "u:",u
            if u==[0]:
            #print "ABC"
                u=[1]
            mat=Householder.multiply_mat(1.0/Householder.InnerProduct(u,u),mat)
        #得到u_T*u
            mat_temp=mat
            mat=Householder.multiply_matrix(mat,R)
        #计算得到R矩阵，也就是本轮的解，R是上一轮运行后得到的R矩阵，这个算法的核心就是R矩阵不断缩小，直到1
            R=Householder.minus_mat(R,Householder.multiply_mat(2,mat))
        #取得本轮缩小后的R矩阵，用于下一轮
            temp=[]
            for d1 in range(len(R)):
                temp_son=[]
                for d2 in range(len(R[0])):
                    if d1>0 and d2>0:
                        temp_son.append(R[d1][d2])
                    else:
                        pass
                if d1==0:
                    pass
                else:
                    temp.append(temp_son)
        #取出下一轮的R后，将剩下的解放入最终的R中，构造最终的R矩阵
        #m和n不同，因此要处理

            Q_temp=[]
            mat_temp=Householder.multiply_mat(2,mat_temp)
        #得到完整的Q矩阵
            I=Householder.construct(len(mat_temp))
            I_1=Householder.minus_mat(I,mat_temp)
        
        #构造出本轮的Q矩阵
            R_temp=Householder.construct(m)
            for i in range(m):
                for j in range(m):
                    if i>=m-len(mat_temp) and j>=m-len(mat_temp):
                        R_temp[i][j]=I_1[i-m+len(mat_temp)][j-m+len(mat_temp)]
                    else:
                        pass
        #print "R_temp:",R_temp
        #更新Q矩阵
            Q_result=Householder.multiply_matrix(R_temp ,Q_result)
        #更新matrix
            matrix=Householder.multiply_matrix(Q_result,matrix_temp)
        #R_result=multiply_matrix(Q_result,matrix)
        #更新R矩阵
            R=temp

#print "Q_result:",Q_result
        #print "matrix:",matrix_temp
        R_result=Householder.multiply_matrix(Q_result,matrix_temp)
        #       print "R_result:",R_result
    
        return Q_result,R_result
            
    @staticmethod
    def solve(matrix):
        Q,R=Householder.Householder_1(matrix)
        print "Q:"
        pprint.pprint(Householder.handleMatrix(Q))
        print "R:"
        pprint.pprint(R)
        print "A:"
        pprint.pprint(Householder.multiply_matrix(Householder.handleMatrix(Q),R))

class Givens:
    @staticmethod
    #两个vector的内积
    def InnerProduct(w,v):
        sum=0
        for i in range(len(w)):
            sum+=w[i]*v[i]
        return sum

    @staticmethod
    #处理vector，使之成为vector的转置
    def handleList(list):
        li=[]
        for i in range(len(list)):
            list_son=[]
            list_son.append(list[i])
            li.append(list_son)
        return li

    @staticmethod
    #处理matrix，行列互换，成为矩阵的转置
    def handleMatrix(matrix):
        mat=[]
        for i in range(len(matrix[0])):
            mat_son=[]
            for j in range(len(matrix)):
                mat_son.append(matrix[j][i])
            mat.append(mat_son)
        return mat

    @staticmethod
    #两个向量的减法
    def minus(in_1,in_2):
        temp=[]
        for i in range(len(in_1)):
            temp_son=in_1[i]-in_2[i]
            temp.append(temp_son)
        return temp

    @staticmethod
    #两个矩阵的减法
    def minus_mat(in_1,in_2):
        temp=in_1
        for i in range(len(in_1)):
            for j in range(len(in_1[0])):
                temp[i][j]-=in_2[i][j]
        return temp

    @staticmethod
    #两个向量的加法
    def add(in_1,in_2):
        temp=[]
        for i in range(len(in_1)):
            temp_son=in_1[i]+in_2[i]
            temp.append(temp_son)
        return temp

    @staticmethod
    #常数和向量的乘法
    def multiply(a,list_b):
        for i in range(len(list_b)):
            list_b[i]=list_b[i]*a
        return list_b
            
    @staticmethod
    #常数和矩阵的乘法
    def multiply_mat(a,matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j]=a*matrix[i][j]
        return matrix

    @staticmethod
    #两个向量的乘法得到一个数，相当于两个向量的内积
    def multiply_list(list_a,list_b):
        list=0
        for i in range(len(list_a)):
            list+=list_a[i]*list_b[i]
        return list

    @staticmethod
    #两个向量相乘得到一个矩阵
    def multiply_list_matrix(list_a,list_b):
        mat=[]
        for i in range(len(list_a)):
            matrix_son=[]
            for j in range(len(list_b)):
                matrix_son.append(list_a[i][0]*list_b[j])
            mat.append(matrix_son)
        return mat

    @staticmethod
    #矩阵和向量相乘
    def multiply_matrix_list(matrix,list):
        list_1=[]
        for i in range(len(matrix)):
            key=0
            for j in range(len(list)):
                key+=matrix[i][j]*list[j]
            list_1.append(key)
        return list_1

    @staticmethod
    #两个矩阵相乘
    def multiply_matrix(matrix_a,matrix_b):
        matrix=[]
        matrix_b=Givens.handleMatrix(matrix_b)
        for i in range(len(matrix_a)):
            matrix_son=[]
            for j in range(len(matrix_b)):
                matrix_son.append(Givens.multiply_list(matrix_a[i],matrix_b[j]))
            matrix.append(matrix_son)
        return matrix

    @staticmethod
    #构造一个n*n的单位矩阵
    def construct(n):
        I=[]
        for i in range(n):
            I_son=[]
            for j in range(n):
                if i==j:
                    I_son.append(1)
                else:
                    I_son.append(0)
            I.append(I_son)
        return I

    @staticmethod
    #在给定c和s的情况下构造G i<j c=xi s=xj
    def construct_G(m,i,j,c,s):
        r=math.sqrt(float(c*c+s*s))
        c=float(c)/r
        s=float(s)/r
        I=[]
        for k in range(m):
            I_son=[]
            for l in range(m):
                if k==l:
                    I_son.append(1)
                else:
                    I_son.append(0)
            I.append(I_son)
        I[i][i]=c
        I[i][j]=s
        I[j][i]=-s
        I[j][j]=c
        return I

    @staticmethod
    def Givens_1(matrix):
    #Use m to constrcut G, but at first, we should handle the matrix to get the column
    #Givens是一种很简单的算法，目标就是不断构建G，将第一列都缩减只有1个元素，第二列缩减到只有2个元素，以此类推。
        m=len(matrix)
        n=len(matrix[0])
    #翻转矩阵，取出每一列
    #R=handleMatrix(matrix)
    #构建最终结果
        R_result=[]
        Q_result=Givens.construct(m)
        for i in range(n):
            R=Givens.handleMatrix(matrix)
            list=R[i]
            for j in range(i,m):
            #如果要处理的两数都为0，就可以不处理
                if list[i]==0 and list[j]==0:
                    pass
                elif i==j:
                    pass
                else:
                #构建G矩阵
                    I=Givens.construct_G(m,i,j,list[i],list[j])
                #更新Q矩阵，I乘以旧的Q
                    Q_result=Givens.multiply_matrix(I,Q_result)
                #print "matrix before:",matrix
                #得到新的R矩阵，只有内层循环结束后，此列才完成
                    matrix=Givens.multiply_matrix(I,matrix)
                #re=multiply_matrix_list(I,list)
                #更新列
                    R=Givens.handleMatrix(matrix)
                    list=R[i]
    #print "I:",I
#print "matrix:",matrix

        return Givens.handleMatrix(Q_result), matrix

    @staticmethod
    def solve(matrix):
        Q,R=Givens.Givens_1(matrix)
        print "Q:"
        pprint.pprint(Q)
        print "R:"
        pprint.pprint(R)
        print "A"
        pprint.pprint(Givens.multiply_matrix(Q,R))


if __name__ == '__main__':
    #将要处理的矩阵 按行输入在这里
    #Matrix=[[1,4,5],[4,18,26],[3,16,30],[1,4,5]]
    Matrix=[[1.0,0,-1.0],[1.0,2.0,1.0],[1.0,1.0,-3.0]]
    #LU分解不适合奇异矩阵，QR分解，Householder和Givens分解可以处理奇异矩阵
    while True:
        t=raw_input("1.LU decomposition\n2.QR decomposition\n3.Householder decomposition\n4.Givens Decomposition\n0.Exit")
        key=["0","1","2","3","4"]
        matrix=[]
        for i in range(len(Matrix)):
            matrix_son=[]
            for j in range(len(Matrix[0])):
                matrix_son.append(Matrix[i][j])
            matrix.append(matrix_son)
    
        if t in key:
            if t=="1":
                LU_1=LU()
                LU_1.solve(matrix)
            elif t=="0":
                break
            elif t=="2":
                QR_1=QR()
                QR_1.solve(matrix)
            elif t=="3":
                QR_2=Householder()
                QR_2.solve(matrix)
            elif t=="4":
                QR_3=Givens()
                QR_3.solve(matrix)
            else:
                pass
        else:
            pass
    print "End!"