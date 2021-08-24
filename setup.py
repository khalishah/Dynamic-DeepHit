import io
import os

from setuptools import setup


def read(file_name):
    """Read a text file and return the content as a string."""
    with io.open(os.path.join(os.path.dirname(__file__), file_name),
                 encoding='utf-8') as f:
        return f.read()

setup(
    name='dynamic_deephit',
    url='https://github.com/khalishah/Dynamic-DeepHit',
    author='Khalishah',
    author_email='khalishah@benshi.ai',
    packages=['dynamic_deephit'],
    install_requires=['funcsigs',
        'numpy',
        'pandas',
        'tensorflow',
        'scikit-learn',
        'lifelines',
        'termcolor'
        'scikit-survival']
    ,
    description='Dynamic-DeepHit',
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
)
    