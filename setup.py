from setuptools import find_packages, setup

setup(
    name='optionsStrategies',
    packages=find_packages(include=['optionsStrategies']),
    version='0.1.0',
    description='Options Strategies library',
    author='Pulkit Gupta| https://www.linkedin.com/in/pulkitgupta31/',
    install_requires=['scipy'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)