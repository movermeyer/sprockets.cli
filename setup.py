from setuptools import setup
import sys

requirements = []
tests_require = ['coverage', 'coveralls', 'nose']

# Requirements for Python 2.6
if sys.version_info < (2, 7):
    requirements.append('argparse')
    requirements.append('importlib')
    requirements.append('logutils')
    tests_require.append('unittest2')
if sys.version_info < (3, 0):
    tests_require.append('mock')


setup(name='sprockets.cli',
      version='0.1.0',
      description='Sprockets command line application runner',
      entry_points={'console_scripts': ['sprockets=sprockets.cli:main']},
      author='AWeber Communications',
      url='https://github.com/sprockets/sprockets.cli',
      install_requires=requirements,
      license=open('LICENSE').read(),
      namespace_packages=['sprockets'],
      package_data={'': ['LICENSE', 'README.rst']},
      packages=['sprockets', 'sprockets.cli'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: No Input/Output (Daemon)',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      test_suite='nose.collector',
      tests_require=tests_require,
      zip_safe=False)
