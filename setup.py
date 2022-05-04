import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fuzzup", 
    version="0.4.3",
    author="Lars Kjeldgaard, Søren Kolbye Jensen",
    author_email="lars.kjeldgaard@eb.dk, soren.k.jensen@eb.dk",
    description="A Fuzzy Matching Approach for Clustering Strings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ebanalyse/fuzzup",
    packages=setuptools.find_packages(include=["fuzzup"]),
    python_requires='>=3.7',
    install_requires=[
        'scipy',
        'pandas>=1.3.5',
        'numpy',
        'rapidfuzz',
        'tqdm'
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
