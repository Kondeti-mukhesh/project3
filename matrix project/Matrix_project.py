import numpy as np
def MatrixOps(promt):
    print(promt)
    rows=int(input("Enter the number of rows:"))
    cols=int(input("Enter the number of columns:"))
    print("Enter the valuess of matrix row by row:")
    matrix=[]

    for i in range(rows):
        row=list(map(float, input(f" Row {i+1}:").split()))
        if len(row)!=cols:
            print("Number of columns must match the input")
            return None
        
        matrix.append(row)
    return np.array(matrix)

def operations():
    while True:
        print("1. Additoin of matrices")
        print("2. Subtraction of matrices")
        print("3. Multiplication of matrices")
        print("4. Transpose of matrices")
        print("5. Determinant of matrices")
        print("6. Exit")

        choice=input("Enter your operation(1-6):")
        if choice == "6":
            break

        mat1=MatrixOps("Matrix 1:")
        mat2=MatrixOps("Matrix 2:")

        if choice == "1":
            if mat1.shape==mat2.shape:
                print("Result:\n",mat1+mat2)
            
            else:
                print("matrix must have the same dimension")

        elif choice == "2":
            if mat1.shape==mat2.shape:
                print("Result:\n",mat1-mat2)
            
            else:
                print("matrix must have the same dimension")
        
        elif choice == "3":
            if mat1.shape[1]==mat2.shape[0]:
                print("Result:\n",np.dot(mat1,mat2))
            
            else:
                print("matrix 1 columns  must have same number of rows in matrix 2")

        elif choice == "4":
            matrix_choice = int(input("Enter 1 for matrix1 or 2 for matrix2: "))

            if matrix_choice == 1:
                print("Transpose of matrix1:\n", np.transpose(mat1))

            elif matrix_choice == 2:
                print("Transpose of matrix2:\n", np.transpose(mat2))

            else:
                print("Invalid choice.")
        
        elif choice == "5":
            if mat1.shape[0] == mat1.shape[1]:
                print("Result:\n", np.linalg.det(mat1))
                
            elif mat2.shape[0] == mat2.shape[1]:
                print("Result:\n", np.linalg.det(mat2))
            else:
                print("Error: Determinant can only be calculated for square matrices.")
        
        else:
            print("Invalid")

if __name__ == "__main__":
    operations()


