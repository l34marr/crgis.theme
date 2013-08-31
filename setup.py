from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='crgis.theme',
      version=version,
      description="CRGIS Theme Package",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://github.com/l34marr/crgis.theme',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['crgis'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
