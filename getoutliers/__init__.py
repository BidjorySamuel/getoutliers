"""

get out, liers😅
====

Outliers it's just a library to identify outliers in a pandas Dataframe and manipulate them

'Made by Samuel Bidjory'

github: https://github.com/BidjorySamuel/getoutliers
"""

__all__ = ["IQR",
           "OutlierManipulater",
           "ZScore",
           "ViewOutliers"
           ]

__version__ = "0.0.4"

from ._zscore import ZScore
from ._iqr import IQR
from ._manipulation import OutlierManipulater
from ._view import ViewOutliers
from ._nan_value import nan_value


