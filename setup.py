import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()

version = '0.10'

setup(
    name='ez_setup',
    version=version,
    description="ez_setup.py and distribute_setup.py",
    long_description=README + '\n\n' + NEWS,
    author='Sridhar Ratnakumar',
    author_email='github@srid.name',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    keywords='ez_setup setuptools distribute workaround',
    url='http://github.com/ActiveState/ez_setup',
    license='PSF or ZPL',
    py_modules=['ez_setup', 'distribute_setup'],
)
