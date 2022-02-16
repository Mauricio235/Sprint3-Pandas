
import pandas as pd

data = [1, 2, 3, 4, 5]
s = pd.Series(data)

index = ["Linha" + str(i) for i in range(5)]

s = pd.Series(data=data, index=index)

data = {'Linha'+str(i):i+1 for i in range(5)}

#Dataframe

data = [[1,2,3], [4,5,6], [7,8,9]]
df1 = pd.DataFrame(data=data)

index = ['Linha' + str(i) for i in range(3)]
df1 = pd.DataFrame(data=data, index=index)


columns = ["Coluna" + str(i) for i in range(3)]
df1 = pd.DataFrame(data=data, index=index, columns=columns)

df2= pd.DataFrame(data=data, index=index, columns=columns)

data = [(1,2,3), (4,5,6), (7,8,9)]
df3= pd.DataFrame(data=data, index=index, columns=columns)

df1[df1>0] = "A"
df2[df2>0] = "B"
df3[df3>0] = "C"

df4 = pd.concat([df1, df2, df3])
df4

df5 = pd.concat([df1, df2, df3], axis=1)
df5




