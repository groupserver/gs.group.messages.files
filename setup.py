# coding=utf-8
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()

setup(name='gs.group.messages.files',
    version=version,
    description="The Files tab in a GroupServer Group",
    long_description=open("README.txt").read() + "\n" +
                      open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
      "Development Status :: 4 - Beta",
      "Environment :: Web Environment",
      "Framework :: Zope2",
      "Intended Audience :: Developers",
      "License :: Other/Proprietary License",
      "Natural Language :: English",
      "Operating System :: POSIX :: Linux"
      "Programming Language :: Python",
      "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='groupserver message post files',
    author='Michael JasonSmith',
    author_email='mpj17@onlinegroups.net',
    url='http://groupserver.org/',
    license='other',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gs', 'gs.group', 'gs.group.messages'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'setuptools',
        'sqlalchemy',
        'zope.cachedescriptors',
        'AccessControl',
        'gs.content.js.jquery',
        'gs.database',
        'gs.group.base',
        'gs.group.home',
        'gs.group.messages.base',
        'Products.GSSearch',
        # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,)
