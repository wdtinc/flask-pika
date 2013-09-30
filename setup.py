"""
Flask-Pika
-------------
Provides a pika channel per request with a single persistant connection per thread to an amqp server
"""
from setuptools import setup


setup(
    name='Flask-Pika',
    version='0.2.2p0',
    url='https://github.com/WeatherDecisionTechnologies/flask-pika',
    license='BSD',
    author='Weather Decision Technologies',
    author_email='alertingdevelopers@wdtinc.com',
    description='Pika amqp flask extension',
    long_description=__doc__,
    zip_safe=False,
    include_package_data=True,
    py_modules=['flask_pika'],
    platforms='any',
    install_requires=[
        'Flask',
        'pika==0.9.14p0'
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
