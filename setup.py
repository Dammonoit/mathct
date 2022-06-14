import os
import sys
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mathct",
    version="1.0.0",
    author="Dharmendra Choudhary",
    author_email="dnc.1124@gmail.com",
    description="Python Library to invoke 100+ mathematical constants",
    long_description=long_description,
    license= 'MIT',
    long_description_content_type="text/markdown",
    url="https://github.com/Dammonoit/mathct",
    project_urls={
        "Bug Tracker": "https://github.com/Dammonoit/mathct/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)