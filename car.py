import pandas as pd
import numpy as np
df1=pd.DataFrame({'Company':['Ford','Mercedes','BMW','Audi'],
                 'price':[23845,171995,135925,71400]})
df2=pd.DataFrame({'Company':['Toyota','Honda','Nissan','Mitsubishi'],
                  'price':[29995,23600,61500,58900]})
data=[df1,df2]
df2=pd.concat(data)
print(df2)
