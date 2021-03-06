import setuptools

setuptools.setup(
    name="sample_qt_error",
    version="0.1",
    install_requires=["qtpy"],
    packages=setuptools.find_packages("./src"),
    package_dir={"": "src"},
    extras_require={
        "test": ["pytest", "pytest-qt"]
    }
)