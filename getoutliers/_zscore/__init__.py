import pandas as pd
import numpy as np
from getoutliers._nan_value import nan_value
class ZScore:
    """
    Z-Score
    ===

    This class, comparating to the other one, zscore is more flexible, because you
    can say to the method what number gonna be the positive and negative limite to zscore
    if zscore is higher or lower the this specific number, it considerating an outlier
    
    """
    def __init__(self, data:pd.Series):
        self.data = np.asanyarray(data)


    def theres_outliers(self, threshold=None, threshold_flexible="mean"):
        
        #If threshold is not None (has to be a number)
        if threshold:
            return self.__zscore(threshold=threshold)
        
        else:
            if threshold_flexible == "min":
                value_with_nan = nan_value.nan_outliers(self.data)
                min_ = np.min(value_with_nan)
                self.__zscore(threshold=min_)
            
            elif threshold_flexible == "max":
                value_with_nan = nan_value.nan_outliers(self.data)
                max_ = np.max(value_with_nan)
                self.__zscore(threshold=max_)

            elif threshold_flexible == "mean":
                value_with_nan = nan_value.nan_outliers(self.data)
                mean = np.mean(value_with_nan)
                self.__zscore(threshold=mean)
            
            elif threshold_flexible == "std":
                value_with_nan = nan_value.nan_outliers(self.data)
                std = np.std(value_with_nan)
                self.__zscore(threshold=std)




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
                

