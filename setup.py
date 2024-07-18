from setuptools import setup, find_packages


with open("README.md", "r") as description:
    description = description.read()



setup(
    name="getoutliers",
    version="0.0.5.3",
    packages=find_packages(),
    url="https://github.com/BidjorySamuel/getoutliers",
    author_email="bidjorysamuel@gmail.com",
    description="`getoutliers` is a Python library designed to identify and manipulate outliers in pandas DataFrames.",
    long_description=description,

    # This package is based on numpy and pandas, so it's really necessary that you install it

    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
    ],
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    # Adicione outras classificações conforme necessário
    # Put others classifiers if it necessary
],

)


