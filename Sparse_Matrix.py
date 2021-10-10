# Name : Sonu Shriram Vishwakarma



# Sparse matrix creation, sparse matrix addition and sparse matrix transpose

def create_matrix(r, c):

    global mat

    mat = []

    for i in range(r):

        row = []

        for j in range(c):

            element = int(input("Enter elements of matrix: "))

            row.append(element)

        mat.append(row)

    return mat

def sparse_matrix(mat,r, c):

    sparse_matrix = []

    tempMat = []

    tempMat.append(len(mat))

    tempMat.append(len(mat[0]))

    sparse_matrix.append(tempMat)

    for i in range(r):

        for j in range(c):

            temp_list = []  

            if mat[i][j]!=0:

                temp_list.append(i) 

                temp_list.append(j)

                temp_list.append(mat[i][j])

                sparse_matrix.append(temp_list)



    tempMat.append(len(sparse_matrix)-1)

    return sparse_matrix



# Triplet matrix addition(sparse)



def sparseAddition(mat1, mat2):

    i=1

    j=1

    addition = []

    l1 = len(mat1)-1

    l2 = len(mat2)-1

    while i<= l1 and j <= l2:

        tempMat = []

        if mat1[i][0]==mat2[j][0]:

            if mat1[i][1]==mat2[j][1]:

                tempMat.append(mat1[i][0])

                tempMat.append(mat1[i][1])

                sum = mat1[i][2]+mat2[j][2]

                tempMat.append(sum)

                addition.append(tempMat)

                i+=1

                j+=1

                #print("tem", tempMat)

                #print("addtion", addition)

            else:

                if mat1[i][1]<mat2[j][1]:

                    tempMat.append(mat1[i][0])

                    tempMat.append(mat1[i][1])

                    tempMat.append(mat1[i][2])

                    addition.append(tempMat)

                    i+=1

                    #print("tem", tempMat)

                    #print("addtion", addition)

                else:

                    if mat1[i][1]>mat2[j][1]:

                        tempMat.append(mat2[j][0])

                        tempMat.append(mat2[j][1])

                        tempMat.append(mat2[j][2])

                        addition.append(tempMat)

                        j+=1

                       # print("tem", tempMat)

                        #print("addtion", addition)

        else:

            if mat1[i][0]>mat2[j][0]:

                tempMat.append(mat2[j][0])

                tempMat.append(mat2[j][1])

                tempMat.append(mat2[j][2])

                addition.append(tempMat)

                j+=1

               # print("tem", tempMat)

                #print("addtion", addition)

            else:

                if mat1[i][0]<mat2[j][0]:

                    tempMat.append(mat1[i][0])

                    tempMat.append(mat1[i][1])

                    tempMat.append(mat1[i][2])

                    addition.append(tempMat)

                    i+=1

                    #print("tem", tempMat)

                    #print("addtion", addition)

    if j == (len(mat2)) and i == (len(mat1)-1):

        tempMat1 = []

        tempMat1.append(mat1[i][0])

        tempMat1.append(mat1[i][1])

        tempMat1.append(mat1[i][2])

        addition.append(tempMat1)

    if j == (len(mat2)-1) and i == (len(mat1)):

        tempMat2 = []

        tempMat2.append(mat2[j][0])

        tempMat2.append(mat2[j][1])

        tempMat2.append(mat2[j][2])

        addition.append(tempMat2)

    return addition



# Sparse transpose :------------->>



def sparseTranspose(sparseMat):

    resultT = []

    tempMat =[]

    tempMat.append(sparseMat[0][1])

    tempMat.append(sparseMat[0][0])

    tempMat.append(sparseMat[0][2])

    resultT.append(tempMat)

    for i in range(sparseMat[0][1]):

        for j in range(1,len(sparseMat)):

            tempMat1 = []

            if i == sparseMat[j][1]:

                tempMat1.append(sparseMat[j][1])

                tempMat1.append(sparseMat[j][0])

                tempMat1.append(sparseMat[j][2])

                resultT.append(tempMat1)

                     

    return resultT





r1 = int(input("Enter number of rows: "))

c1 = int(input("Enter number of columns: "))

mat1=create_matrix(r1,c1)



r2 = int(input("Enter number of rows: "))

c2 = int(input("Enter number of columns: "))

mat2=create_matrix(r2,c2)











s_mat1=sparse_matrix(mat1,r1, c1)

s_mat2=sparse_matrix(mat2,r2, c2)

print("sparse Matrix 1: \n",sparse_matrix(mat1,r1, c1))

print("sparse Matrix 2: \n",sparse_matrix(mat2,r2, c2))

print("Addition: \n",sparseAddition(s_mat1, s_mat2))

print("Transepose of ", sparse_matrix(mat1,r1, c1), " is: ", sparseTranspose(s_mat1))
