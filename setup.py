import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="meta",
    version="0.0.1",
    author="Jianwei Han",
    author_email="hanjianwei@gmail.com",
    description="Get metadata from various websites",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hanjianwei/meta",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
    ],
    entry_points={
        "console_scripts": ["meta = meta.cmd:main"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
