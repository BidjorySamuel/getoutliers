"""

get out, liers😅
====

Outliers it's just a library to identify outliers in a pandas Dataframe and manipulate them

'Made by Samuel Bidjory'

github: https://github.com/BidjorySamuel/getoutliers
"""

__version__ = "0.0.3"

from getoutliers.__outlier_detections import *
from getoutliers.__outlier_manipulation import OutlierManipulater
from getoutliers.__outlier_visualization import ViewOutliers

__all__ = ["IQR",
           "OutlierManipulater",
           "ZScore",
           "ViewOutliers"
           ]