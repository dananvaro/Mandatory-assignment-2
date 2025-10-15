from setuptools import setup, find_packages

setup(
    name="Schedule reminder",
    version="1.0",
    packages=find_packages(),  
    py_modules=['main'],       
    include_package_data=True,
    description="Mandatory assignment 2 for ACIT4420 Problem-solving with scripting",
    author="Danan Subramaniam",
    author_email="dasub6503@oslomet.no",
    install_requires=[],
    entry_points={
    "console_scripts": [
            "schedule-reminder = main:main",  
        ],
    },
)