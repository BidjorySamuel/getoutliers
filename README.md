### README for IQR Outlier Detection Module

---

## IQR Outlier Detection

The `IQR` module is designed to help identify outliers in a dataset using the Interquartile Range (IQR) method. This module was created by Samuel Bidjory.

### Description

The IQR (Interquartile Range) is a measure of statistical dispersion, or how spread out the values in a dataset are. It is defined as the difference between the 75th percentile (Q3) and the 25th percentile (Q1) of the data. This method is commonly used to detect outliers. Values that fall below Q1 - 1.5 * IQR or above Q3 + 1.5 * IQR are considered outliers.

### Installation

To use this module, you need to have Python installed along with the `numpy` library. You can install `numpy` using pip:

```bash
pip install numpy
```

### Usage

Below are the methods provided by the `IQR` class and how to use them:

1. **Initialization**:
    ```python
    from getoutliers import IQR
    import numpy as np

    data = np.array([1, 2, 3, 4, 5, 30])
    iqr_detector = IQR(data)
    ```

2. **Interquartile Range Calculation**:
    ```python
    iqr = iqr_detector.iqr
    print(iqr)  # Output: {'Q1': 2.0, 'Q3': 4.0, 'result': 2.0}
    ```

3. **Check Lower Bound Outliers**:
    ```python
    has_lower_bound_outliers = iqr_detector.there_lb()
    print(has_lower_bound_outliers)  # Output: False or True
    ```

4. **Check Upper Bound Outliers**:
    ```python
    has_upper_bound_outliers = iqr_detector.there_up()
    print(has_upper_bound_outliers)  # Output: False or True
    ```

5. **Check for Any Outliers**:
    ```python
    outliers_info = iqr_detector.theres_outliers()
    print(outliers_info)
    # Output: {'there_up?': True, 'up_iqr': 7.0} or other relevant info based on the data
    ```

6. **Get Specific Outliers**:
    ```python
    specific_outliers = iqr_detector.theres_outliers(value=True)
    print(specific_outliers)
    # Output: {'index': array([5]), 'value': 30}
    ```

### Methods

- `iqr`: Property that calculates and returns the interquartile range (IQR) along with Q1 and Q3.
- `there_lb(bool_=True)`: Checks for lower bound outliers. Returns a boolean indicating presence of outliers if `bool_` is `True`, otherwise returns the lower bound value.
- `there_up(bool_=True)`: Checks for upper bound outliers. Returns a boolean indicating presence of outliers if `bool_` is `True`, otherwise returns the upper bound value.
- `theres_outliers(value=False)`: Checks for any outliers in the dataset. If `value` is `False`, returns information on whether there are any outliers and their respective bounds. If `value` is `True`, returns the actual outliers in the dataset.

### Examples

**Example 1: Basic Usage**
```python
data = [1, 2, 3, 4, 30]
iqr_detector = IQR(data)
print(iqr_detector.iqr)  # Output: {'Q1': 2.0, 'Q3': 4.0, 'result': 2.0}
print(iqr_detector.theres_outliers())  # Output: {'there_up?': True, 'up_iqr': 7.0}
```

**Example 2: Getting Specific Outliers**
```python
data = [1, 2, 3, 4, 30]
iqr_detector = IQR(data)
print(iqr_detector.theres_outliers(value=True))  # Output: {'index': array([4]), 'value': 30}
```

### License

This project is licensed under the MIT License.

### Author

Samuel Bidjory

---# getoutliers
