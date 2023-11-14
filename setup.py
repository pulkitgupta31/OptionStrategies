from setuptools import find_packages, setup

VERSION = '0.1.1'
DESCRIPTION = 'Options Strategies library'
LONG_DESCRIPTION = 'A package that allows you to calculate the payoff and profit/loss of various options strategies.'

setup(
    name='optionsStrategies',
    packages=find_packages(include=['optionsStrategies']),
    version=VERSION,
    description=DESCRIPTION,
    author='Pulkit Gupta| https://www.linkedin.com/in/pulkitgupta31/',
    author_email="<iampulkit31@gmail.com>",
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packeges=find_packages(),
    install_requires=['scipy'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    keywords=['options', 'strategies', 'payoff', 'profit', 'loss'],
)