from setuptools import setup, find_packages
import sys
import os
from pathlib import Path

CURRENT_DIR = Path(__file__).parent


def get_long_description():
    "Read in the README file"
    return (CURRENT_DIR / "README.md").read_text(encoding="utf8")


setup(
    name="padeiro",
    use_scm_version=True,
    description="The sourdough bread baker's assistant",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    keywords="bread sourdough baker recipe",
    author="Leonardo Uieda",
    author_email="leouieda@gmail.com",
    url="https://github.com/leouieda/padeiro",
    license="MIT",
    packages=find_packages(exclude=["doc", "tests"]),
    python_requires=">=3.6",
    install_requires=["click>=6.5", "pooch>=0.7.0", "toml>=0.9.4"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Home Automation",
    ],
    entry_points={"console_scripts": ["padeiro=padeiro.cli:main"]},
)
