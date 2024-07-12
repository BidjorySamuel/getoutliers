

from getoutliers._iqr import IQR
import numpy as np


def nan_outliers(data):
        """Replace outliers with NaN values."""

        data = np.asanyarray(data)

        if data.dtype != "float64":
            data = data.astype("float64")
        iqr = IQR(data)
        outliers = iqr.theres_outliers(value=True)
        
        if outliers is None or "index" not in outliers:
            raise ValueError("The IQR method did not return the expected result with 'index'")
        
        # Garante que os índices sejam do tipo array de inteiros
        # Substitui os valores nos índices especificados por np.nan
        data[outliers["index"]] = np.nan
        return data

   