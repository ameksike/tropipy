import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tropipy",
    version="0.0.1",
    author="Antonio Membrides Espinosa, Sergio Daniel",
    author_email="tonykssa@gmail.com",
    description="TropiPay SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ameksike/tropipy",
    project_urls={
        "Bug Tracker": "https://github.com/ameksike/tropipy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)