#!/usr/bin/env python

# How to build source distribution
# python setup.py sdist --format bztar
# python setup.py sdist --format gztar
# python setup.py sdist --format zip

import os
from setuptools import setup

# Check the Python version
import sys
major, minor, micro, s, tmp = sys.version_info
if major==2 and minor<7 or major<2:
    raise SystemExit("""Requires Python 2.7 or later.""")
if major==3:
    raise SystemExit("""Doesn't work on Python 3...""")

setup(name="py_megablast",
      version="0.2"
      description="Wrapper for megablast",
      author="Louis-Philippe Lemieux Perreault",
      author_email="louis-philippe.lemieux.perreault@statgen.org",
      url="http://www.statgen.org",
      license="GPL",
      scripts=[os.path.join("scripts", "py_megablast"),],
      install_requires=["biopython >=1.62", "numpy >= 1.7.1"],
##       packages=["pyGenClean", "PlinkUtils", "pyGenClean.Misc"] +
##                ["pyGenClean.Step{}".format(i) for i in xrange(1, 13)],
      classifiers=['Operating System :: Linux',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.7'])
