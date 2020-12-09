import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="multiSrcDict", # Replace with your own username
    version="0.0.1",
    author="Huang Hing Pang",
    author_email="huanghingpang@gmail.com",
    description="Python multi-source dict",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThomasHuang168/multiSrcDict.git",
    install_requires=[openpyxl]
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Text Processing',
    ],
    python_requires='>=3.6',
    license="MIT",
)