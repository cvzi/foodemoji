import setuptools
import os
import io

with io.open("README.md", encoding="utf-8") as f:
    long_description = f.read().strip()

version = None
with io.open(os.path.join("foodemoji", "__init__.py"), encoding="utf-8") as f:
    for line in f:
        if line.strip().startswith("__version__"):
            version = line.split("=")[1].strip().replace('"', "").replace("'", "")
            break

setuptools.setup(
    name="german-foodemoji",
    version=version,
    author="cuzi",
    author_email="cuzi@openmail.cc",
    description="Decorate German text with food specific emojis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cvzi/foodemoji",
    packages=["foodemoji"],
    package_dir={"foodemoji": "foodemoji"},
    package_data={"foodemoji": ["foodemojis.json"]},
    zip_safe=True,
    test_suite="nose.collector",
    tests_require=["emoji", "nose"],
    classifiers=(
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Communications :: Chat",
        "Topic :: Printing",
        "Topic :: Text Processing :: General"
    ),
)
