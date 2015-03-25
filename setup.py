import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

README = open('README.rst').read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-simple-user',
    version='0.1',
    packages=['custom_auth'],
    include_package_data=True,
    install_requires=[
        "Django >= 1.5",
    ],
    license='BSD License',
    description='Very simple user model for Django >= 1.5 with only email and password fields.',
    long_description=README,
    url='https://github.com/Seleznev-nvkz/django-simple-user/',
    author='Konstantin Seleznev',
    author_email='seleznev.nvkz@gmail.com',
    keywords='django user auth model',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)