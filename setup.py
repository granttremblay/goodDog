try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A Python module to make X-ray Spectral maps of Temperature, Density, and Entropy for Chandra Observations of Galaxy Clusters',
    'author': 'Grant R. Tremblay & Dominic A. Eggerman',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'grant.tremblay@yale.edu',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)