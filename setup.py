from setuptools import setup, find_packages



setup(
    name="getoutliers",
    version="0.0.5.1",
    packages=find_packages(),
    url="https://github.com/BidjorySamuel/getoutliers",
    author_email="bidjorysamuel@gmail.com",

    # This package is based on numpy and pandas, so it's really necessary that you install it

    requires=[
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
],

)


