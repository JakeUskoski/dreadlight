import os

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dreadlight",
    version="0.1.12",
    author="Jake Uskoski",
    author_email="jake@uskoski.ca",
    description="A terminal-based moddable RPG",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JakeUskoski/dreadlight",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "dreadlight = dreadlight.__main__:main",
            "dl = dreadlight.__main__:main"
        ]
    },
)
