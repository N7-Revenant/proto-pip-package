"""PyPI Package Prototype"""
import os

from setuptools import setup, find_packages

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

setup(
    name='pypi-package',
    version='0.0.0',
    description='PyPI Package Prototype',
    packages=find_packages(os.path.join(PROJECT_ROOT, 'src')),
    package_dir={"": 'src'},
    namespace_packages=['hl_namespace', 'hl_namespace.ll_namespace'],
    entry_points={
        'console_scripts': [
            'module-name-main = hl_namespace.ll_namespace.module_name:main']},
    install_requires=[],
    python_requires='>=3.8',
    zip_safe=True,

    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Education",
        "License :: Free For Educational Use",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8"],
)
