import numpy as np
import pandas as pd
from getoutliers._iqr import IQR
from getoutliers._manipulation import ManiOut1D
from _dtypes.types import Dtype2DOutlier



class IqrMultiD(Dtype2DOutlier):
    """
    IQR Multi-Dimensional (pandas DataFrame)
    ------

    detect outlier in a pandas dataframe,
    using IQR (1.5) method.

    """
    

    @property
    def iqr(self) -> pd.DataFrame:

        #Create a dictionary to store others dictionaries
        iqrs = {}

        for col in self.columns:

            iqr_detector = IQR(self.data[col])

            result = iqr_detector.iqr

            iqrs[col]  = result

        return pd.DataFrame(iqrs)

            


    
    def theres_outliers(self) -> pd.DataFrame:
        """
        This method gonna select the numerics columns, 
        the index gonna begin at the first numeric column,
        the index 1 gonna be the second numeric column and so one...

        
        """

        outliers = {}
        index_column_count = 0

        for col in self.columns:

            iqr_detector = IQR(self.data[col])

            result = iqr_detector.theres_outliers(value=True)

            if result is None: # If there's no outliers...
                continue       # Skip

            text = {"index": np.array([index_column_count, int(result["index"])]), "value":result["value"]}

            outliers[col] = text

            index_column_count += 1

        return pd.DataFrame(outliers)
    


class ManiOut2D(Dtype2DOutlier):
    """
    
    Manipulate Outlier for 2-Dimensional Data (pandas DataFrame)
    
    """

    def nan_outliers(self):
        
        # Create a new dict to put each numeric columns into him
        # And after, convert it in a pandas DataFrame
        new_df = {}

        for col in self.columns:
            # Im using the OutlierManipulater to nan outliers in each numeric columns
            iqr_manipulating = ManiOut1D(self.data[col]) 

            new_df[col] = iqr_manipulating.nan_outliers()

        return pd.DataFrame(new_df)
    


    def fill_outliers(self):
        # fill outliers in a basic way, if you want it to be more flexible
        # Just use nan_outliers and use "fillna" with more flexibility
        
        nan_numbers = self.nan_outliers()

        nan_numbers.fillna(method="ffill", inplace=True)

        return nan_numbers
    

    
    def remove_outliers(self):

        # Remove outliers in a basic way, if you want it to be more flexible
        # Just use nan_outliers and use "dropna" with more flexibility
        nan_numbers = self.nan_outliers()

        nan_numbers.dropna(inplace=True)

        return nan_numbers








        

    
