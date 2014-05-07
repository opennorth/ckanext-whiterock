from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-whiterock',
    version=version,
    description="Customization for City of White Rock",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='St\xc3\xa9phane Guidoin',
    author_email='stephane@opennorth.ca',
    url='',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.whiterock'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        # myplugin=ckanext.whiterock.plugin:PluginClass
    ''',
)
