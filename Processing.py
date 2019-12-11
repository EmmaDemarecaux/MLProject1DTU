import numpy as np
import xlrd
import pandas as pd


df = pd.read_excel('wage.xls', header = None)
doc = xlrd.open_workbook('wage.xls').sheet_by_index(0)

attributeNames = doc.row_values(0, 1, 8)
n = len(df.index)
df.reset_index()
df.reindex(index=range(0,n))
     
df.dropna(inplace=True)
dfMatrix = df.values

y = dfMatrix[1:,0]
yMatrix = np.mat(y)

N = len(y)
M = len(attributeNames)

X = np.mat(np.empty((N,M)))

for i, col_id in enumerate(range(1,M+1)):
    X[:,i] = np.matrix(doc.col_values(col_id, 1, n)).T
