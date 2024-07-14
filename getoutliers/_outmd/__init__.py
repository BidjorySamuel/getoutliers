import numpy as np
import pandas as pd
from getoutliers._iqr import IQR



class OutlierMultiD:
    """
    Outlier Multi-Dimensional (pandas DataFrame)
    ------

    detect outlier in a pandas dataframe,
    using IQR (1.5) method.


    """
    def __init__(self, data:pd.DataFrame):
        self.data = data

    

    def getoutlier(self):
        """
        This method gonna select the numerics columns, 
        the index gonna begin at the first numeric column,
        the index 1 gonna be the second numeric column and so one...

        
        """

        numeric_columns = self.data.select_dtypes(np.number)
        columns = numeric_columns.columns

        outliers = []
        index_column_count = 0

        for col in columns:

            iqr_detector = IQR(numeric_columns[col])

            result = iqr_detector.theres_outliers(value=True)

            text = {"index": np.array([index_column_count, int(result["index"])]), "value":result["value"]}

            outliers.append(text)

            index_column_count += 1

        return outliers