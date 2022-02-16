
import pandas as pd

data = [1, 2, 3, 4, 5]
s = pd.Series(data)

index = ["Linha" + str(i) for i in range(5)]

s = pd.Series(data=data, index=index)

data = {'Linha'+str(i):i+1 for i in range(5)}

