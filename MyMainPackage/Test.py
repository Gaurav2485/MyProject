import numpy as np
import pandas as pd

reviews=pd.read_csv("/Users/kiaan/Documents/Project/nyse_data/test.csv",header=None,sep=',', lineterminator='\n')
# reviews.to_csv("/Users/kiaan/Documents/Project/nyse_data/test.csv",sep=',', mode='a')
reviews.head()