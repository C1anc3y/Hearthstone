#!/usr/bin/env python
# encoding: utf-8
"""
@File: setup.py
@Author: ClanceyHuang
@Time: 19-3-4 上午8:57
@Desc:  ...
@Version: Python3
"""
import logging
from setuptools import setup, find_packages

readme_file = 'README.md'

try:
    import pypandoc
    long_description = pypandoc.convert(readme_file, to='rst')
except ImportError:
    logging.warning('pypandoc module not found, long_description will be the raw text instead.')
    with open(readme_file, encoding='utf-8') as fp:
        long_description = fp.read()

setup(
    name='Hearthstone',
    version='0.0.1',
    packages=find_packages(),
    package_data={
        '': ['*.md'],
        'Hearthstone': ['career_names.json']
    },
    include_package_data=True,
    install_requires=[
        'requests>=2.0',
        'scrapy>=1.0'
    ],
    url='https://github.com/ClanceyHuang/Hearthstone',
    license='MIT',
    author='ClanceyHuang',
    author_email='ClanceyHuang@gmail.com',
    description='用数据玩炉石！快速收集和分析炉石传说的卡牌及卡组数据。',
    long_description=long_description,
    keywords=[
        '炉石',
        'Hearthstone',
        '数据'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: MIT',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Topic :: Games/Entertainment :: Simulation',
        'Topic :: Scientific/Engineering :: Information Analysis'
    ]
)
