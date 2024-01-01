from setuptools import find_packages, setup

setup(
    name="KatCorner",
    version="0.1",
    packages=find_packages(exclude=["project_test"]),
    include_package_data=True,
    description="A simple Django app for kat data. Imports into Kats application.",
    long_description="README.md",
    url="https://github.com/brucestull/kat-corner",
    author="Flynnt Knapp",
    author_email="FlynntKnapp@gmail.com",
    license="MIT",
    install_requires=[
        "django>=3.0",
    ],
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
    ],
)
