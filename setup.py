import re
import ast
from setuptools import setup
from flask_pluginkit_isso import __version__, __author__, __license__, __description__


def _get_author():
    mail_re = re.compile(r'(.*)\s<(.*)>')
    return (mail_re.search(__author__).group(1), mail_re.search(__author__).group(2))


(author, email) = _get_author()
setup(
    name='flask-pluginkit-isso',
    version=__version__,
    license=__license__,
    author=author,
    author_email=email,
    url='https://github.com/flask-pluginkit/flask-pluginkit-isso',
    download_url="https://github.com/flask-pluginkit/flask-pluginkit-isso/releases",
    keywords="flask-pluginkit",
    description=__description__,
    packages=['flask_pluginkit_isso'],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'Flask-PluginKit>=3.0.0',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
