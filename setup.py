from setuptools import setup, find_packages

setup(
    name="rwanda-locations-api",
    version="1.0.0",
    description="A FastAPI package with all Rwanda's location data from provinces to villages",
    author="MWIMULE Bienvenu",
    author_email="mwimulebienvenu05@gmail.com",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn"
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "rwanda-api = rwanda_locations.api:app"
        ]
    }
)
