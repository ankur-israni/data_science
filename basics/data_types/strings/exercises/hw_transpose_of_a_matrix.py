# Find the transpose of a 2 dimensional array
# Transpose = converting rows in columns

list_2d_array = [[1,2], [3,4]]
# transpose = [[1,3],[2,4]
transpose = [[]]

# Print the whole 2D array using for loop
def simplePrintOf2DMatrix():
    print("****** Simple printing of 2D matrix ******")
    for row in list_2d_array:
        for col in row:
            print(col)
    return;



# Print matrix using rows and columns
def printMatrixUsingRowsAndColumns():
    print("****** Print 2D matrix using rows and columns ******")
    rowindex = 0
    for row in list_2d_array:
        colindex = 0
        for col in row:
            if(rowindex > len(list_2d_array)):
                   break
            print("element , row, column = ",list_2d_array[rowindex][colindex],rowindex,colindex)
            colindex += 1
        rowindex += 1



# Transpose of a 2D matrix using for loop
def transposeOf2DMatrix():
    for row in range(len(list_2d_array)): #  This is 1st row = [0,1],
        print("row=",row);
        newList = []
        for item in list_2d_array:
            print("item=",item)
            print("item[row]=",item[row])
            newList.append(item[row])
            transpose.append(newList)
    print("transponse = ",transpose)

origionalMatrix = [[4, 5, 3, 9], [7, 1, 8, 2], [5, 6, 4, 7]]
#origionalMatrix=[[1,2], [3,4]]
transposedMatrix = []
def transpose():
    for i in range(len(origionalMatrix)):
        transposedRow = []
        for origionalRow in origionalMatrix:
            transposedRow.append(origionalRow[i]) # 'origionalRow[i]' is an individual elmement in the 'transposedRow'

        transposedMatrix.append(transposedRow) #In outer for loop
    print("transposedMatrix = ",transposedMatrix)


'''
# Transpose of a 2D matrix - Not working - 
print("****** Transpose of a matrix using rows and columns ******")
rowindex = 0
for row in list_2d_array:
    colindex = 0
    for col in row:
        if(rowindex > len(list_2d_array)):
               break
        print("element , row, column = ",list_2d_array[rowindex][colindex],rowindex,colindex)
        if(rowindex==colindex):
            # transpose[rowindex,colindex]=list_2d_array[rowindex][colindex]
            transpose[rowindex][colindex] = list_2d_array[rowindex][colindex]
            print("equal = ",list_2d_array[rowindex][colindex])
        elif(rowindex != colindex):
            transpose[colindex][rowindex] = list_2d_array[rowindex][colindex]
            print("notequal = ", list_2d_array[rowindex][colindex])
        colindex += 1
    rowindex += 1
'''



# Execution block
transpose()
#simplePrintOf2DMatrix()
#transposeOf2DMatrix();

