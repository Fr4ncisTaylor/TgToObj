import pathlib
from setuptools import setup

# This call to setup() does all the work
setup(
    name="tg-to-obj",
    version="1.0.0",
    description="Make a telegram api dict update to obj.",
    long_description='README.md',
    long_description_content_type="text/markdown",
    url="https://github.com/francis-taylor/TgToObj",
    author="Francis Taylor",
    author_email="Francistrapp2000@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["tg_to_obj"],
    include_package_data=True,
    install_requires=["requests", "beautifulsoup4"],
    entry_points=None
)