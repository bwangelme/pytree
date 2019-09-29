# -*- coding: utf-8 -*-

from setuptools import setup

version = "0.1"

install_requires = ['graphviz', 'PyYAML']

setup(name='pytree',
      version=version,
      description='Draw Tree from YAML',
      author="bwangel",
      author_email="bwangel.me@gmail.com",
      url='http://github.com/bwangelme/pytree',
      install_requires=install_requires,
      license='MIT',
      zip_safe=False,
      entry_points="""
      [console_scripts]
      pytree = pytree.tree:main
      """,
)


