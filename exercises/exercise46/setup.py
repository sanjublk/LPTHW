try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'My project',
        'author': 'Me',
        # 'url': 'URL to get it at',
        # 'download_url': 'Where to download it.',
        'version': '0.1',
        'install_requires': ['pytest'],
        'packages': ['hellworld'],
        'scripts': [],
        'name': 'projectname'
        }
setup(**config)
