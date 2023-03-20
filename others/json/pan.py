import pandas as pd
 
inp = [{'c1':10, 'c2':100}, {'c1':11, 'c2':110}, {'c1':12, 'c2':123}]
df = pd.DataFrame(inp)
 
# iterrows
for date, row in df.iterrows():
    print(date,row, row['c1'], row['c2'])
 
# iteritems
for date, row in df.iteritems():
    print(row[0], row[1], row[2])
 
# itertuples
for row in df.itertuples():
    print(getattr(row, 'c1'), getattr(row, 'c2'))
