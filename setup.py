from setuptools import setup, find_packages


setup(
    name="python-sample-lib",
    version='1.0.0',
    description='サンプルライブラリ',
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    license='MIT',
)
