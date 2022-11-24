import pandas as pd
import numpy as np
df1=pd.DataFrame({'company':['Toyota','Honda','BMW','Audi'],
                   'price':[23845,17995,135925,71400]})
df2=pd.DataFrame({'company':['Toyota','Honda','BMW','Audi'],
                     'horsepower':[141,80,182,160]})
print (pd.merge(df1,df2,on='company') )  
a=df2['horsepower']
df1=df1.join(a)
print(df1)