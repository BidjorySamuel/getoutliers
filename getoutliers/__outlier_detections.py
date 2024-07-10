
import numpy as np
import pandas as pd

class IQR:
    """
    IQR
    ===

    It's a class for identify outliers in pandas dataframe

    """
    def __init__(self, data: np.ndarray) -> np.ndarray:
        #Convert the data as an numpy array to be able to work with pandas Dataframe
        self.data = np.asanyarray(data)
        

    

    @property
    def iqr(self):
        """
        The IQR is the 75% of the Series of number minus the 25%

        IQR = Q3 - Q1
        
        >>> x = [1, 2, 3, 4, 5]
        2 (Q1) is the 25% and 4 (Q3) is the 75 %

        """
        Q1 = np.percentile(self.data, 25)
        Q3 = np.percentile(self.data, 75)

        return {"Q1":Q1, "Q3":Q3, "result":Q3 - Q1}

        
    
    def there_lb(self, bool_=True):
        """
        there_lb = "there lower bound"

        The lower bound is the method that gonna say to you,
        if in the specific dataset (pandas Series) has lower bound outliers or not.
        
        """
        iqr = self.iqr["result"]

        q1 = self.iqr["Q1"]

        result = (True if min(self.data) < q1 - 1.5 * iqr else False)

        if bool_ == True:
            return result
        elif bool_ == False:
            return q1 - 1.5 * iqr
        else:
            raise "The value has to be a boolean type, it works with 1 or 0"
    
    def there_up(self, bool_=True):
        """
        there_up = "there upper bound"

        The upper bound is the method that gonna say to you,
        if in the specific dataset (pandas Series) has upper bound outliers or not.
        
        """

        iqr = self.iqr["result"]

        q3 = self.iqr["Q3"]

        result = (True if max(self.data) > q3 + 1.5 * iqr else False)

        if bool_ == True:
            return result
        elif bool_ == False:
            return q3 + 1.5 * iqr
        else:
            raise "The value has to be a boolean type, it works with 1 or 0"
        
        
    def theres_outliers(self, value=False):
        """
        there is outliers ? i dunno
        ---------------------------
        that function gonna answer that question to you.

        If the dataset has outliers, it gonna return a dict that contains
        a boolean value (there_lb? or there_up?) that said if it has (outliers) or not and a
        real number (up_iqr ou lb_iqr).

        If the dataset has a upper bound:

        >>> list = [1, 2, 3, 4, 30]
        >>> x = getoutliers.IQR(list)
        >>> x.there_outliers()
        {'there_up?': True, 'up_iqr': np.float64(7.0)}

        If the dataset has a lower bound:
        >>> list = [-10, 2, 3, 4, 5]
        >>> x = getoutliers.IQR(list)
        >>> x.there_outliers()
        {'there_lb?': True, 'lb_iqr': np.float64(-10)}
        
        """

        if value == False:

            #Check if there two outliers lower bound and upper bound
            #there_outliers gonna return a dict cointains the values of
            #lower bound and upper bound
            if self.there_lb() == True and self.there_up() == True:
                return {"there_lb?":True, "lb_iqr":self.there_lb(bool_=False), "there_up?":
                        True, "up_iqr":self.there_up(bool_=False)}

            #Check if there is a lower bound
            elif self.there_lb() == True:
                return {"there_lb?":True, "lb_iqr":self.there_lb(bool_=False)}
            
            #Check if there is a upper bound
            elif self.there_up() == True:
                return {"there_up?":True, "up_iqr":self.there_up(bool_=False)}
            
            
            
            else:
                return self.data
            

        # If the value is True, that gonna return just the value (outliers) of the dataset    
        elif value == True:
            if self.there_lb() == True:
                result = np.where((self.data < self.there_lb(bool_=False)))
                return {"index":result, "value":self.data[result][0]}
            
            elif self.there_up() == True:
                result =  np.where((self.data > self.there_up(bool_=False)))
                return {"index":result, "value":self.data[result][0]}
        

        
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


    def theres_outliers(self, threshold=None, threshold_flexible=""):
        
        #If threshold is not None (has to be a number)
        if threshold:
            return self.__zscore(threshold=threshold)
        
        else:
            if threshold_flexible == "min":
                min_ = self.data.min()
                value = self.__zscore(threshold=min_)
            
            elif threshold_flexible == "max":
                max_ = self.data.max()
                value = self.__zscore(threshold=max_)

            elif threshold_flexible == "mean":
                mean = self.data.mean()
                value = self.__zscore(threshold=mean)
            
            elif threshold_flexible == "std":
                std = self.data.std()
                value = self.__zscore(threshold=std)

            return value




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
                




    


