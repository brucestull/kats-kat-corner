from setuptools import find_packages, setup

setup(
    name="KatCorner",
    version="0.1",
    packages=find_packages(exclude=["project_test"]),
    include_package_data=True,
    description="A simple Django app for kat data. Imports into Kats application.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",  # Add this if README.md is Markdown
    python_requires=">=3.7",  # Optional: helps restrict bad installs
    url="https://github.com/brucestull/kats-kat-corner",
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
