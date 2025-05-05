from setuptools import setup

setup(
    name='FileOrganizer',
    version='1.0',
    py_modules=['organize'],
    entry_points={
        'console_scripts': ['fileorganizer=organize:main'],
    },
    install_requires=['python-magic'],
    python_requires='>=3.10',
)
