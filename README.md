# getoutliers: get out, liers

[![getoutliers - Pypi](https://badge.fury.io/py/getoutliers.svg)](https://badge.fury.io/py/getoutliers)

`getoutliers` is a Python library designed to identify and manipulate outliers in pandas DataFrames. It offers various methods based on IQR and Z-Score to detect outliers and functionalities to effectively replace or remove them.

## Installation

To install the package, use:

```sh
pip install getoutliers
```

## Usage

### Importing the Module

```python
from getoutliers import IqrMultiD, IQR, ManiOut2D, ManiOut1D, ZScore
import pandas as pd
```

### Sample Data

```python
dados = {
    "nome": ["Sam", "Dudu", "Pedro", "John", "Don", "Ben"],
    "Idade": [23, 20, 23, 200, 23, 12],
    "Salario": [2300, 2500, 2300, 2400, 45000, 2600]
}

x = [12, 13, 15, 13, 150]
df = pd.DataFrame(dados)
```

### Using `ManiOut2D` to Remove Outliers

```python
maniout = ManiOut2D(df)
print(maniout.remove_outliers())
```

### Class: `IQR`

The `IQR` class identifies outliers in a pandas DataFrame using the Interquartile Range method.

#### Methods

- **iqr**: Calculates the IQR of the data.
- **there_lb**: Checks for lower bound outliers.
- **there_up**: Checks for upper bound outliers.
- **theres_outliers**: Determines if there are any outliers.

### Class: `ManiOut1D`

The `ManiOut1D` class manipulates outliers in a pandas DataFrame.

#### Methods

- **nan_outliers**: Replaces outliers with NaN values.
- **fill_outliers**: Fills NaN values (former outliers) with specified statistical measures (mean, median, mode).
- **fill**: Convenience method that combines `nan_outliers` and `fill_outliers`.
- **remove_outliers**: Removes outliers by dropping NaN values.

### Class: `IqrMultiD`

The `IqrMultiD` class detects outliers in a multi-dimensional pandas DataFrame using the IQR method.

#### Methods

- **iqr**: Calculates the IQR for each column.
- **theres_outliers**: Identifies outliers in each column.

### Class: `ZScore`

The `ZScore` class detects outliers using the Z-Score method.

#### Methods

- **theres_outliers**: Identifies outliers based on a specified Z-Score threshold.

### Class: `ViewOutliers`

The `ViewOutliers` class visualizes outliers in a pandas DataFrame.

#### Methods

- **boxplot**: Displays a boxplot and returns IQR and median values.

## Example

```python
import numpy as np
from getoutliers import ManiOut2D, IqrMultiD

dados = {
    "nome": ["Sam", "Dudu", "Pedro", "John", "Don", "Ben"],
    "Idade": [23, 20, 23, 200, 23, 12],
    "Salario": [2300, 2500, 2300, 2400, 45000, 2600]
}

df = pd.DataFrame(dados)
manipulator = ManiOut2D(df)
cleaned_data = manipulator.remove_outliers()
print(cleaned_data)
```

## Contribution

If you would like to contribute to this module, feel free to open a pull request or report issues on the GitHub repository.

## License

This project is licensed under the MIT License.

## Author

`getoutliers` was created by Samuel Bidjory.

GitHub: [getoutliers](https://github.com/BidjorySamuel/getoutliers)
