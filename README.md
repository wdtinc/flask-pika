#Pika Extension for Flask
This extension provides a simple way to expose a Pika channel per request over a per thread connection to an AMQP server.

Once a channel is obtained, use it as you would any normal Pika channel.

##Initializing the Pika object
Simply initialize the Flask Pika instance with the app and a Pika connection params object.

	from flask import Flask
	from flask.ext.pika import Pika as FPika

	app = Flask(__name__)
    app.config['PIKA_PARAMS'] = {
	        'host':'amqp host', //amqp.server.com
            'username': 'username',
            'password': 'password',
			'port': 5672, //amqp server port
	        'virtual_host':'vhost' //amqp vhost
    }
	fpika = FPika()
	fpika.init_app(app)
	
##Using the Pika object
Use the pika object you created and get a channel.

	fpika.channel.basic_publish(exchange='exchange',routing_key='routing_key',body='message')
		
Flask Pika will create a channel per request and take care of closing it for you on request end.
