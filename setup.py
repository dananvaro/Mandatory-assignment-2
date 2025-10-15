from setuptools import setup, find_packages

setup(
    name="Schedule reminder",
    version="1.0",
    packages=find_packages(),  # Includes the 'games' package
    py_modules=['main'],       # Includes main.py as a top-level module
    include_package_data=True,
    description="A fun game module as a part of ACIT4420 the lecture series. Basically from Lecture 5, 6, and 7.",
    author="Danan Subramaniam",
    author_email="dasub6503@oslomet.no",
    install_requires=[],
    entry_points={
        'console_scripts': [
            'schedule-reminder=main:main',  # Points to main() in main.py (root directory)
        ],
    },
)