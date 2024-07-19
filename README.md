# getoutliers: get out, liers

[![getoutliers - Pypi](https://badge.fury.io/py/getoutliers.svg)](https://badge.fury.io/py/getoutliers)

`getoutliers` is a Python library designed to identify and manipulate outliers in pandas DataFrames. It offers various methods based on IQR and Z-Score to detect outliers and functionalities to effectively replace or remove them.

## Installation

To install the package, use:

```sh
pip install getoutliers
```

## Modules and Classes

### 1. IQR

The `IQR` class is designed to identify outliers in pandas series using the Interquartile Range (IQR) method.

#### Usage:

```python
from getoutliers import IQR
import numpy as np

data = np.array([1, 2, 3, 4, 5, 30])
iqr = IQR(data)

# Check IQR values
print(iqr.iqr)
```

#### Output:

```python
{'Q1': 2.0, 'Q3': 5.0, 'result': 3.0}
```

```python
# Check for lower bound outliers asking: "there lower bound?"
print(iqr.there_lb())
```

#### Output:

```python
False
```

```python
# Check for upper bound outliers
print(iqr.there_up())
```

#### Output:

```python
True
```

```python
# Get outlier information
print(iqr.theres_outliers())
```

#### Output:

```python
{'there_up?': True, 'up_iqr': 9.5}
```

### 2. OutlierManipulater

The `OutlierManipulater` class provides methods to manipulate outliers in pandas series, converting them to NaN values, filling them with specific methods, or removing them.

#### Usage:

```python
from getoutliers import OutlierManipulater
import pandas as pd

data = pd.Series([1, 2, 3, 4, 5, 30])
manipulater = OutlierManipulater(data)

# Replace outliers with NaN
print(manipulater.nan_outliers())
```

#### Output:

```python
0    1.0
1    2.0
2    3.0
3    4.0
4    5.0
5    NaN
dtype: float64
```

```python
# Fill NaN values (previous outliers) with the mean
print(manipulater.fill_outliers(method="mean"))
```

#### Output:

```python
0     1.0
1     2.0
2     3.0
3     4.0
4     5.0
5     3.0
dtype: float64
```

```python
# Easily fill outliers directly
print(manipulater.fill(method="median"))
```

#### Output:

```python
0     1.0
1     2.0
2     3.0
3     4.0
4     5.0
5     3.0
dtype: float64
```

```python
# Remove outliers
print(manipulater.remove_outliers())
```

#### Output:

```python
0    1.0
1    2.0
2    3.0
3    4.0
4    5.0
dtype: float64
```

### 3. ZScore

The `ZScore` class detects outliers based on the Z-Score method, allowing flexibility to set thresholds.

#### Usage:

```python
from getoutliers import ZScore
import pandas as pd

data = pd.Series([1, 2, 3, 4, 5, 30])
zscore = ZScore(data)

# Detect outliers with a custom threshold
print(zscore.theres_outliers(threshold=2))
```

#### Output:

```python
{'mean': 7.5,
 'stdev': 11.079688818055006,
 'zscore': array([-0.58667515, -0.49690382, -0.40713249, -0.31736115, -0.22758982,
         2.03566243]),
 'outliers': array([30])}
```

```python
# Detect outliers with flexible threshold based on the mean
print(zscore.theres_outliers(threshold_flexible="mean"))
```

#### Output:

```python
{'mean': 7.5,
 'stdev': 11.079688818055006,
 'zscore': array([-0.58667515, -0.49690382, -0.40713249, -0.31736115, -0.22758982,
         2.03566243]),
 'outliers': array([30])}
```

### 4. ViewOutliers

The `ViewOutliers` class provides visualization for outliers in pandas series using boxplots.

#### Usage:

```python
from getoutliers import ViewOutliers
import pandas as pd

data = pd.Series([1, 2, 3, 4, 5, 30])
view = ViewOutliers(data)

# Display boxplot and return IQR and median values
print(view.boxplot(save="boxplot.png"))
```

#### Output:

The boxplot graph will be saved as `boxplot.png`.

```python
(array([30]), 3.5) # 30 is the outlier and 3.5 is the median
```

### 5. IqrMultiD

The `IqrMultiD` class detects outliers in multi-dimensional pandas DataFrames using the IQR method.

#### Usage:

```python
from getoutliers import IqrMultiD
import pandas as pd

data = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 30],
    'B': [10, 20, 30, 40, 50, 100]
})
iqr_multi = IqrMultiD(data)

# Get IQR values for each numeric column
print(iqr_multi.iqr)
```

#### Output:

```python
           A     B
Q1       2.0  20.0
Q3       5.0  50.0
result   3.0  30.0
```

```python
# Get outliers for each numeric column
print(iqr_multi.getoutlier())
```

#### Output:

```python
        A         B
index  [0, 5]     [1, 5]
value  [30]       [100]
```

### 6. Function `nan_outliers`

The `nan_outliers` function replaces outliers in a numpy array with NaN values.

#### Usage:

```python
from getoutliers import nan_outliers
import numpy as np

data = np.array([1, 2, 3, 4, 5, 30])
print(nan_outliers(data))
```

#### Output:

```python
array([ 1.,  2.,  3.,  4.,  5., nan])
```

## Contributing

If you wish to contribute to this module, feel free to fork the repository and submit a pull request. Contributions are always welcome!

## Author

`getoutliers` was created by Samuel Bidjory.

GitHub: [getoutliers](https://github.com/BidjorySamuel/getoutliers)
