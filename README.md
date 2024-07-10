# getoutliers or get out, liers 😅

## Overview
The `getoutliers` module is a Python package designed to identify and manipulate outliers in pandas DataFrames using statistical methods such as IQR (Interquartile Range) and Z-Score. This module provides a set of classes to help with detecting and handling outliers, offering flexibility and ease of use for data preprocessing.

## Installation

To install the module, simply clone this repository and install the dependencies (pip package soon).

```bash
git clone https://github.com/BidjorySamuel/getoutliers.git
cd getoutliers
pip install -r requirements.txt
pip install e .
```

## Usage

### IQR Class

The `IQR` class identifies outliers using the Interquartile Range method.

#### Methods

- **__init__(self, data: np.ndarray)**: Initializes the class with the input data.

- **iqr**: Computes the IQR, returning Q1 (25th percentile), Q3 (75th percentile), and the IQR value.
    ```python
    x = IQR([1, 2, 3, 4, 5])
    print(x.iqr)  # {'Q1': 2, 'Q3': 4, 'result': 2}
    ```

- **there_lb(self, bool_=True)**: Checks if there are lower bound outliers. Returns a boolean or the lower bound value based on the `bool_` parameter.

- **there_up(self, bool_=True)**: Checks if there are upper bound outliers. Returns a boolean or the upper bound value based on the `bool_` parameter.

- **theres_outliers(self, value=False)**: Determines if there are any outliers and returns their details. If `value` is True, returns the outlier values directly.

### ZScore Class

The `ZScore` class identifies outliers using the Z-Score method.

#### Methods

- **__init__(self, data: pd.Series)**: Initializes the class with the input data.

- **theres_outliers(self, threshold=None, threshold_flexible="")**: Determines outliers based on a specified threshold or flexible threshold (min, max, mean, std).

- **__zscore(self, threshold)**: Private method to compute the Z-Score and identify outliers.

### OutlierManipulater Class

The `OutlierManipulater` class manipulates outliers in a pandas DataFrame.

#### Methods

- **__init__(self, data: Series)**: Initializes the class with the input data.

- **nan_outliers(self)**: Replaces outliers with NaN values.
    ```python
    om = OutlierManipulater(pd.Series([1, 2, 3, 4, 30]))
    print(om.nan_outliers())  # Outliers replaced with NaN
    ```

- **fill_outliers(self, method="mean")**: Fills NaN values (former outliers) using a specified method (mean, median, mode).

- **fill(self, method="mean")**: A convenience method that replaces outliers with NaN and fills them using the specified method.

- **remove_outliers(self)**: Placeholder for a method to remove outliers (not implemented).

### ViewOutliers Class

The `ViewOutliers` class provides visualization for outliers in a pandas DataFrame.

#### Methods

- **__init__(self, data: pd.Series)**: Initializes the class with the input data.

- **boxplot(self)**: Displays a boxplot of the data and returns the IQR and median values.
    ```python
    vo = ViewOutliers(pd.Series([1, 2, 3, 4, 30]))
    vo.boxplot()  # Displays boxplot
    ```

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request on GitHub.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



By following these instructions, you can easily identify and handle outliers in your dataset, ensuring cleaner and more reliable data for your analysis and modeling tasks.
