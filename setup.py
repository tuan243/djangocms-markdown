import os
from setuptools import setup, find_packages


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="djangocms-markdown",
    version='0.3.0',
    description=read('DESCRIPTION'),
    long_description=read('README.md'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, django-cms, plugin, markdown, editor',
    author='Olle Vidner',
    author_email='olle@vidner.se',
    url="https://github.com/ovidner/djangocms-markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django',
        'South',
        'django-cms>=3.0.0',
        'django-markdown-deux',
    ],
)
