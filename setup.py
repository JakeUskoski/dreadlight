import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gladiator-jake-uskoski",  # Replace with your own username
    version="0.1.0",
    author="Jake Uskoski",
    author_email="jake@uskoski.ca",
    description="A terminal-based moddable RPG",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/juskoski/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
