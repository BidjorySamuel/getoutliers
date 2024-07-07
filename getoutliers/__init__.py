"""

get out, liers😅
====

Outliers it's just a library to identify outliers in a pandas Dataframe and manipulate them

'Made by Samuel Bidjory'

github: https://github.com/BidjorySamuel/BidjorySamuel
"""

__version__ = "0.0.3"

from getoutliers.__iqr import IQR
from getoutliers.__outlier import Outlier_manipulater

__all__ = ["IQR",
           "Outlier_manipulater",
           ]