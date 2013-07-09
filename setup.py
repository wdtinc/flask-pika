"""
Flask-AMQP
-------------
Provides an amqp channel (via Pika) per request with a single persistant connection per thread to an amqp server
"""
from setuptools import setup


setup(
    name='Flask-AMQP',
    version='1.0',
    url='',
    license='',
    author='Karl Kirch',
    author_email='kkirch@wdtinc.com',
    description='Pika amqp flask extension',
    long_description=__doc__,
    py_modules=['flask_amqp'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'pika==0.9.13'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
