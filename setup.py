from setuptools import setup, find_packages

setup(
    name="rwanda-locations-api",
    version="1.1.1",
    description="API package containing all regions of Rwanda from provinces to villages.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="MWIMULE Bienvenu",
    author_email="mwimulebienvenu05@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
