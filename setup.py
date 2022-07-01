import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fuzzup",
    version="0.4.9",
    author="Lars Kjeldgaard, Søren Kolbye Jensen",
    author_email="lars.kjeldgaard@eb.dk, soren.k.jensen@eb.dk",
    description="A Fuzzy Matching Approach for Clustering Strings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ebanalyse/fuzzup",
    packages=setuptools.find_packages(include=["fuzzup"]),
    python_requires=">=3.7",
    install_requires=[
        "scipy==1.8.1",
        "pandas>=1.3.5",
        "numpy==1.21.6",
        "rapidfuzz==2.0.4",
        "tqdm==4.64.0",
        "cvr==0.2.0",
        "geopy==2.2.0",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    include_package_data=True,
)
