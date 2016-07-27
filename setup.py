try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A Python module to make X-ray Spectral maps of Temperature, Density, and Entropy for Chandra Observations of Galaxy Clusters',
    'author': 'Grant R. Tremblay & Dominic A. Eggerman',
    'url': 'https://github.com/granttremblay/goodDog',
    'download_url': 'https://github.com/granttremblay/goodDog',
    'author_email': 'grant.tremblay@yale.edu',
    'version': '0.1dev',
    'install_requires': ['nose','CIAO'],
    'packages': ['goodDog'],
    'scripts': [],
    'name': 'goodDog'
}

setup(**config)