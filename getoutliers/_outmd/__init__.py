import numpy as np
import pandas as pd
from getoutliers._iqr import IQR



class IqrMultiD:
    """
    IQR Multi-Dimensional (pandas DataFrame)
    ------

    detect outlier in a pandas dataframe,
    using IQR (1.5) method.

    """
    def __init__(self, data:pd.DataFrame):
        # I have to do that in the moment, but i'm really working
        # about that.
        # The concern is, that's gonna select just numeric columns.
        # And it gonna returns just those numeric columns.
        self.data = data.select_dtypes(np.number)


    @property
    def iqr(self) -> pd.DataFrame:

        columns = self.data.columns
        #Create a dictionary to store others dictionaries
        iqrs = {}

        for col in columns:

            iqr_detector = IQR(self.data[col])

            result = iqr_detector.iqr

            iqrs[col]  = result

        return pd.DataFrame(iqrs)

            


    
    def getoutlier(self) -> pd.DataFrame:
        """
        This method gonna select the numerics columns, 
        the index gonna begin at the first numeric column,
        the index 1 gonna be the second numeric column and so one...

        
        """

        columns = self.data.columns

        outliers = {}
        index_column_count = 0

        for col in columns:

            iqr_detector = IQR(self.data[col])

            result = iqr_detector.theres_outliers(value=True)

            text = {"index": np.array([index_column_count, int(result["index"])]), "value":result["value"]}

            outliers[col] = text

            index_column_count += 1

        return pd.DataFrame(outliers)