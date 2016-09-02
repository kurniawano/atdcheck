from setuptools import setup, find_packages
from codecs import open
from os import path

here=path.abspath(path.dirname(__file__))
with open(path.join(here,'README.md'),encoding='utf-8') as f:
	long_description=f.read()

setup(
	name='atdcheck',
	version='1.0.4',
	description='A Python wrapper for ATD (After The Dateline)',
	long_description=long_description,
	url='https://github.com/kurniawano/atdcheck',
	author='Oka Kurniawan',
	author_email='oka@okakurniawan.net',
	license='MIT',
	classifiers=[
	'Development Status :: 4 - Beta',
	'Intended Audience :: Education',
	'Topic :: Utilities',
	'License :: OSI Approved :: MIT License',
	'Programming Language :: Python :: 2.7',
	],
	keywords='tools utilities spell grammar check',
	packages=find_packages(exclude=['contrib', 'docs', 'tests']),
	entry_points={
	'console_scripts':[
	'atdcheck=atdcheck.__main__:main',
	],
	}
	)