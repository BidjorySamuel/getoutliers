import pandas as pd
from getoutliers import IQR
import matplotlib.pyplot as plt

class ViewOutliers:
    def __init__(self, data:pd.Series):
        self.data = data

    # Boxplot method gonna be more flexible in a soon future
    def boxplot(self):
        """
        Boxplot
        ====

        It gonna show a grafic of your Pandas Series, and it going to return as well a tuple of
        the iqr and median values
        
        """
        plt.boxplot(self.data)
        plt.show()
        iqr = IQR(self.data).theres_outliers(value=True)["value"]
        median = self.data.median()
        return iqr, median
    
