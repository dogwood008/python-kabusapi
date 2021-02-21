from setuptools import setup
from setuptools import find_packages

# https://buildersbox.corp-sansan.com/entry/2019/07/11/110000

setup(
    name="kabusapi",
    version="1.0.0",
    install_requires=["requests", "websockets"],
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
