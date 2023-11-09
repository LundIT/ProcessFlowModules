from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="LundProcessFlowModules",
    version="1.0.0",
    author="Melih Sünbül",
    author_email="m.sunbul@lund-it.com",
    description="A Python library to use 3rd party APIs in your project directly",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LundIT/ProcessFlowModules",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
