import numpy as np
import random 

#np.random.seed(2)
#matrix = np.random.randint(1,100,(5,5))
'''print("The Matrix is:\n", matrix)
print("The Shape is:\n", matrix.shape)
print("The Maximum is:\n", matrix.max())
print("The Minimum is:\n", matrix.min())
print("The Average is:\n",np.mean(matrix))
print("The Sum is:\n",np.sum(matrix))

print(matrix[0,:])
print(matrix[:,4])
print(matrix[1:4,1:4])

greater_than_50 = []
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if matrix[i,j] > 50:
            greater_than_50.append(matrix[i,j])
print("Numbers greater than 50:\n",greater_than_50)

less_than_50 = []
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if matrix[i,j] < 50:
            less_than_50.append(matrix[i,j])
print("Numbers less than 50:\n",less_than_50)

replaceWith0 = []
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if matrix[i,j] < 30:
            replaceWith0.append(matrix[i,j])
            matrix[i, j] = 0
print("Replaced with 0:\n",replaceWith0)

print("The sum of Each collum\n",np.sum(matrix, axis=0))  
print("The sum of each row\n",np.sum(matrix, axis=1))
print("The mean of Each collum\n",np.mean(matrix, axis=0) )
print("The sum of the each row\n",np.mean(matrix, axis=1))
print("The max of Each collum \n",np.max(matrix, axis=0))  
print("The min of Each row\n",np.min(matrix, axis=1))'''


'''''numbers = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

greate_than_50 = numbers[numbers>50]
less_than_50 = numbers[numbers<50]

print(greate_than_50)
print(less_than_50)'''
'''def splitnumbers(num , limit):
    greater = []
    lesser = []
    for i in num:
        if i > limit:
            greater.append(i)
    for i in num:
        if i < limit:
            lesser.append(i)
    return greater, lesser

numbers = [73, 83, 76, 96, 76, 86, 64, 91, 68, 52, 41, 16, 39, 28]
greater , lesser = splitnumbers(numbers , 50)

print(greater)
print(lesser)'''

'''for i in range(len(numbers)):
    currentnumber = numbers[i]

    if 50 < currentnumber:
        greater_than_50.append(currentnumber)
    print(greater_than_50)

for j in range(len(numbers)):
    currentnumber = numbers[j]

    if 50 > currentnumber:
        less_than_50.append(currentnumber)
    print(less_than_50)'''



import pandas as pd

data = {
    "Name": ["Ayan", "Mina", "Rafi", "Sara"],
    "Age": [23, 21, 25, 20],
    "Score": [88, 92, 79, 95]
}

df = pd.DataFrame(data)
print(df)
print(df["Name"])          # single column
print(df[["Name", "Age"]]) # multiple columns

print(df[df["Age"] > 21])  # filtering
print(df[df["Score"] >= 90])
