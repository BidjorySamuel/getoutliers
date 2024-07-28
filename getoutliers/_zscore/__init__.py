import pandas as pd
import numpy as np
from _dtypes.types import DType1DOutlier


class ZScore(DType1DOutlier):
    """
    Z-Score
    ===

    This class, comparating to the other one, zscore is more flexible, because you
    can say to the method what number gonna be the positive and negative limite to zscore
    if zscore is higher or lower the this specific number, it considerating an outlier
    
    """


    def theres_outliers(self, threshold=None):
        
        #If threshold is not None (has to be a number)
        if threshold:
            return self.__zscore(threshold=threshold)
        



    def __zscore(self, threshold):
        mean = self.data.mean()
        stdev = self.data.std()

        # That's the z-score formula
        result = (self.data - mean) / stdev

        #And now i said, if the z-score is higher than the threshold or the result 
        # Is lower than the negative(threshold), that's gonna be considered as an outlier
        check_outlier = self.data[(result > threshold) | (result < (-threshold))]

        return {"mean":mean,
                "stdev":stdev,
                "zscore":result,
                "outliers":check_outlier}
