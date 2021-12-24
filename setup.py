from setuptools import setup, find_packages

setup(
    name="e_library",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "elib = app.cli:cli",
        ],
    },
)
