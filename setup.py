import setuptools
import pypipe


with open("README.md", "r") as fh:
    long_description = fh.read()


with open("requirements.txt", "r") as fh:
    dependencies = fh.read()


setuptools.setup(
    name="pypipe",
    version=pypipe.VERSION,
    author="Marcus Lind",
    author_email="marcuslind90@gmail.com",
    description="A framework for data scientists",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypipe/pypipe",
    packages=setuptools.find_packages(),
    install_requires=dependencies,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
