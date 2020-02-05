import setuptools

setuptools.setup(
    name="xl",
    packages=["xl"],
    version="0.0.2",
    test_suite="tests",
    install_requires=["pandas", "xlrd"],
    entry_points={"console_scripts": ["xl=xl:main"]},
)
