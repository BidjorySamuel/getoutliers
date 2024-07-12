from setuptools import setup, find_packages



setup(
    name="getoutliers",
    version="0.0.4",
    packages=find_packages(where="getoutliers"),
    package_dir={"":"getoutliers"},

    # This package is based on numpy and pandas, so it's really necessary that you install it

    requires=[
        "numpy",
        "pandas",
        "matplotlib",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent",
    ],

)


