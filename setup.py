import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="metasoup",
    version="0.0.1",
    author="Jianwei Han",
    author_email="hanjianwei@gmail.com",
    description="Get metadata from various websites",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hanjianwei/book-metasoup",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
