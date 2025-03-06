from setuptools import setup, find_packages
from codecs import open
import os


scriptFolder = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptFolder)

with open('README.md', 'r') as readme_file:
    readme_content = readme_file.read()


setup(
    name='pybenpytest',
    version='1.0.0',
    description='PyBEN pytest plugin to add an "invalid" test result',
    long_description=readme_content,
    long_description_content_type='text/markdown',
    url='https://github.com/DarkFlameBEN/pybenpytest.git',
    author='Ben Moskovitch',
    author_email='"Ben Moskovitch" <darkflameben@gmail.com>',
    license="MIT",
    classifiers=[
        "Framework :: Pytest",
        "Programming Language :: Python :: 3",
    ],
    install_requires=['pytest'],
    include_package_data=True,
    packages=find_packages(exclude=['tests']),
    python_requires='>3',
    entry_points={"pytest11": ["invalid = pybenpytest.pyben_pytest_invalid"]},
)
