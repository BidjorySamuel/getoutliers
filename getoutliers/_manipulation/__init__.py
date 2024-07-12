"""
If anyone who whant to contribute in this module, go ahead!

It's the more revelant module, cause that can manipulate a outliers in a pandas dataframe

"""
from pandas import Series
from getoutliers._iqr import IQR
import numpy as np

class OutlierManipulater():
    """
    OM = Outlier_manipulater
    =====

    This class is for manipulate outliers in a pandas DataFrame
    You can transform a outliers in a nan number, You can fill
    Those nan numbers whose considering a outliers for
    Outlier_manipulater
    
    """
    def __init__(self, data:Series):
        self.data = Series(data)


    def nan_outliers(self):
        """Replace outliers with NaN values."""
        iqr = IQR(self.data)
        outliers = iqr.theres_outliers(value=True)
        
        if outliers is None or "index" not in outliers:
            raise ValueError("The IQR method did not return the expected result with 'index'")
        
        index = outliers["index"]
        self.data.loc[index] = np.nan
        return self.data
    

    def fill_outliers(self, method="mean"):
        """Fill NaN values (former outliers) with a specified method.
        
        Method options:
        - mean
        - median
        - mode

        But to use fill_outliers function, you must use nan_outliers method firstly, it's obligatory,
        But if you don't want to do all this, you must use "fill" method.
        """
        if method not in ["mean", "median", "mode"]:
            raise ValueError(f"Method '{method}' not in the options")

        if method == "mean":
            fill_value = self.data.mean()
        elif method == "median":
            fill_value = self.data.median()
        elif method == "mode":
            fill_value = self.data.mode()[0]

        self.data.fillna(fill_value, inplace=True)
        return self.data
    

    def fill(self, method="mean") -> None:
        """
        That's method it's just for lazy people
        who don't want to use nan_outliers
        for using fill_outliers, because,
        if you want to use fill_outliers, you'd
        have to use "nan_outliers".
        """
        self.nan_outliers()
        self.fill_outliers(method=method)

        return self.data
    
    def remove_outliers(self):
        #remove outliers normally, with dropna method in pandas,
        #We tranformed outliers in nan, and after we use dropna
        #To remove nan values.
        self.nan_outliers()
        self.data.dropna(inplace=True)
        return self.data
