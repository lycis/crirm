try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'CRIteria REMove. Delete files based on various criteria like age, file size etc.',
    'author': 'Daniel Eder',
    'url': 'http://github.com/lycis/crirm',
    'download_url': 'http://github.com/lycis/crirm',
    'author_email': 'daniel@deder.at',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['crirm'],
    'scripts': [],
    'name': 'crirm'
}

setup(**config)