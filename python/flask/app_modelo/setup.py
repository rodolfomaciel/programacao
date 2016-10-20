# documentacao http://flask.pocoo.org/docs/0.11/patterns/distribute/ e http://flask.pocoo.org/docs/dev/tutorial/setuptools/
from setuptools import setup

setup(
    name='flaskr',
    packages=['flaskr'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
