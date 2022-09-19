"""Setup script for pm_stats package."""
from setuptools import find_packages
from setuptools import setup


setup(
    name="pm_stats",  # update this to reflect your project name
    version="1.0.0",
    description="Code for pm_stats package",
    author="James Trimarco",  # change this to your name or org
    author_email="james.trimarco@gmail.com",  # change this to your email
    install_requires=[],
    include_package_data=True,
    package_dir={"": "src"},  # this is required to access code in src/
    packages=find_packages(where="src"),  # same as above
)
