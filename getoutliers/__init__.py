"""

get out, liers😅
=======
Outliers it's just a library to identify outliers in a pandas Dataframe and manipulate them

'Made by Samuel Bidjory'

github: https://github.com/BidjorySamuel/getoutliers
"""

__all__ = ["IQR",
           "OutlierManipulater",
           "ZScore",
           "ViewOutliers",
           "IqrMultiD",
           "nan_value"
           ]

__version__ = "0.0.5.1"


from ._zscore import ZScore
from ._iqr import IQR
from ._manipulation import ManiOut1D
from ._view import ViewOutliers
from ._outmd import IqrMultiD, ManiOut2D
from ._nan_value import nan_value





