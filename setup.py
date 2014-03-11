"""
Flask-Pika
-------------
This extension provides a simple way to expose a Pika blocking channel inside of Flask.

Once a channel is obtained, use it as you would any normal Pika blocking channel.
"""
from setuptools import setup


setup(
    name='Flask-Pika',
    version='0.3.2',
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
        'Flask>=0.7',
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
