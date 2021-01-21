import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FuzzUp", 
    version="0.0.5",
    author="Lars Kjeldgaard",
    author_email="lars.kjeldgaard@eb.dk",
    description="A Fuzzy Matching Approach for Clustering Strings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ebanalyse/fuzzup",
    packages=setuptools.find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires='>=3.6',
    install_requires=[
        'scipy',
        'pandas',
        'numpy',
        'fuzzywuzzy'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest',
                   'pytest-cov'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    include_package_data=True
    )