
# getoutliers or get out, liers 😅

## Overview

`getoutliers` is a Python module designed to identify and handle outliers in a dataset using the Interquartile Range (IQR) method. This module can be particularly useful for data preprocessing in data science and machine learning projects.

## Features

- **IQR Calculation**: Calculate the Interquartile Range to detect potential outliers.
- **Outlier Detection**: Determine if there are outliers in the dataset.
- **Outlier Handling**: Replace outliers with NaN values and fill them with specified methods (mean, median, mode).

## Installation

To install the module, simply clone this repository and install the dependencies (pip package soon).

```bash
git clone https://github.com/BidjorySamuel/getoutliers.git
cd getoutliers
pip install -r requirements.txt
```

## Usage

### IQR Class

The `IQR` class is used to calculate the Interquartile Range and detect outliers.

#### Initialization

```python
import numpy as np
from getoutliers import IQR

data = np.array([1, 2, 3, 4, 5, 30])
iqr = IQR(data)
```

#### IQR Property

Calculates the Interquartile Range (IQR) which is the difference between the 75th percentile (Q3) and the 25th percentile (Q1).

```python
iqr_values = iqr.iqr
print(iqr_values)
# Output: {'Q1': 2.0, 'Q3': 4.0, 'result': 2.0}
```

#### Lower Bound Detection

Checks if there are any lower bound outliers (values significantly lower than the 25th percentile minus 1.5 times the IQR).

```python
has_lower_bound_outliers = iqr.there_lb()
print(has_lower_bound_outliers)
# Output: False
```

#### Upper Bound Detection

Checks if there are any upper bound outliers (values significantly higher than the 75th percentile plus 1.5 times the IQR).

```python
has_upper_bound_outliers = iqr.there_up()
print(has_upper_bound_outliers)
# Output: True
```

#### Outlier Information

Provides detailed information about the outliers, indicating whether there are lower or upper bound outliers and their respective values.

```python
outliers_info = iqr.theres_outliers()
print(outliers_info)
# Output: {'there_up?': True, 'up_iqr': 7.0}
```

### Outlier Manipulator Class

The `Outlier_manipulater` class is used to handle outliers in a pandas DataFrame.

#### Initialization

```python
import pandas as pd
from getoutliers import Outlier_manipulater

data = pd.Series([1, 2, 3, 4, 5, 30])
om = Outlier_manipulater(data)
```

#### Replace Outliers with NaN

Identifies and replaces outliers with NaN values.

```python
data_with_nan = om.nan_outliers()
print(data_with_nan)
# Output: 0     1.0
#         1     2.0
#         2     3.0
#         3     4.0
#         4     5.0
#         5     NaN
#         dtype: float64
```

#### Fill NaN Values

Fills NaN values (former outliers) with a specified method (mean, median, mode).

```python
filled_data = om.fill_outliers(method="mean")
print(filled_data)
# Output: 0     1.0
#         1     2.0
#         2     3.0
#         3     4.0
#         4     5.0
#         5     3.0
#         dtype: float64
```

#### Combined Method

Automatically replaces outliers with NaN and fills them with the specified method.

```python
om.fill(method="mean")
print(om.data)
# Output: 0     1.0
#         1     2.0
#         2     3.0
#         3     4.0
#         4     5.0
#         5     3.0
#         dtype: float64
```

## Contributing

If you wish to contribute to this module, feel free to fork the repository and submit a pull request. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

By following these instructions, you can easily identify and handle outliers in your dataset, ensuring cleaner and more reliable data for your analysis and modeling tasks.