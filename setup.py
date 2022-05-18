# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
# (c) Ericsson 2022 - All Rights Reserved
#
# No part of this material may be reproduced in any form
# without the written permission of the copyright owner.
# The contents are subject to revision without notice due
# to continued progress in methodology, design and manufacturing.
# Ericsson shall have no liability for any error or damage of any
# kind resulting from the use of these documents.
#
# Any unauthorized review, use, disclosure or distribution is
# expressly prohibited, and may result in severe civil and
# criminal penalties.
#
# Ericsson is the trademark or registered trademark of
# Telefonaktiebolaget LM Ericsson. All other trademarks mentioned
# herein are the property of their respective owners.
#
# ------------------------------------------------------------------------------
from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


def version():
    with open('VERSION.info') as f:
        return f.read().strip()


def requirements():
    with open('requirements.txt') as f:
        return f.readlines()


setup(
    name='cda_test_automation',
    version=version(),
    description='__THIS_IS_USED_FOR_DEVELOPMENT_ONLY__',
    long_description=readme(),
    url='https://url',
    author='__NOBODY__',
    author_email='__NOBODY__@ericsson.com',
    packages=find_packages(),
    install_requires=requirements(),
    include_package_data=True,
    package_data={'': ['*.zip']},
    zip_safe=False,
)