"""
Flask-Migrate
--------------

SQLAlchemy database migrations for Flask applications using Alembic.
"""
from setuptools import setup


setup(
    name='Flask-Migrate',
    version='0.1.0',
    url='http://github.com/miguelgrinberg/flask-migrate/',
    license='MIT',
    author='Miguel Grinberg',
    author_email='miguelgrinberg50@gmail.com',
    description='SQLAlchemy database migrations for Flask applications using Alembic',
    long_description=__doc__,
    py_modules=['flask_migrate'],
    zip_safe=False,
    data_files=[('templates/flask', ['templates/flask/alembic.ini.mako', 'templates/flask/env.py', 'templates/flask/README', 'templates/flask/script.py.mako'])],
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.9',
        'Flask-SQLAlchemy>=1.0',
        'alembic>=0.6',
        'Flask-Script>=0.6'
    ],
    test_suite = "tests",
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)