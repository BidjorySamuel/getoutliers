import pandas as pd
import numpy as np



class DType1DOutlier: #Data Type Uni-D Outlier
    
    def __init__(self, data):
        #Convert the data as an numpy array to be able to work with pandas Dataframe
        self.data = pd.Series(data)
        
        




class Dtype2DOutlier: #Data type Multi-Dimensional Outlier
    
    def __init__(self, data:pd.DataFrame):
        # I have to do that in the moment, but i'm really working
        # about that.
        # The concern is, that's gonna select just numeric columns.
        # And it gonna returns just those numeric columns.
        self.data = pd.DataFrame(data).select_dtypes(np.number)
        
        self.columns = self.data.columns



    
