import setuptools

setuptools.setup(
    name = 'xl',
    packages = ['xl'],
    version = '0.0.3',
    install_requires = ['pandas', 'xlrd'],
    entry_points = {"console_scripts" : ["xl=xl:main"]},
)
