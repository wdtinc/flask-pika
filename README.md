#Pika Extension for Flask
This extension provides a simple way to expose a Pika blocking channel inside of Flask.

Once a channel is obtained, use it as you would any normal Pika blocking channel.

##Initializing the Pika object
Add the Flask Pika Params to your app config and then initialize the Flask Pika instance with a your app instance.

    ##config.py
    FLASK_PIKA_PARAMS = {
        'host':'amqp host',      #amqp.server.com
        'username': 'username',  #convenience param for username
        'password': 'password',  #convenience param for password
        'port': 5672,            #amqp server port
        'virtual_host':'vhost'   #amqp vhost
    }

    # optional pooling params
    FLASK_PIKA_POOL_PARAMS = {
        'pool_size': 8,
        'pool_recycle': 600
    }


    ##app.py
    from flask import Flask
	from flask.ext.pika import Pika as FPika

    app = Flask(__name__)
	fpika = FPika(app)

    # Alternatively, Flask's application factory pattern is supported:
    
    fpika = Fpika()
    # Then, later...
    fpika.init_app(app)


##Connection pooling
If the optional FLASK_PIKA_POOL_PARAMS are specified in your app config, then channels will be allocated via a pool of channels.

* pool_size: number of channels to have open at any one time
* pool_recycle: amount of time in seconds before a channel is closed and it's replaced in the pool (internally this is done on checkout)

Each pool will be allocated per process and the pool will be shared amongst the threads in the process.
	

##Using the Pika object
Use the pika object you created and get a Pika blocking channel.
    
    ch = fpika.channel();
	ch.basic_publish(exchange='exchange',routing_key='routing_key',body='message')
    fpika.return_channel(ch);


##Resource handling
Any pika channel obtained via the fpkia.channel() call must be returned via either the fpika.return_channel(channel) call 
or the fpika.return_broken_channel(channel) call.

The return_channel call should be used under normal circumstances and the return_broken_channel call should be used if the 
channel is known to be broken.

If the return channel calls are not used, then Pika connections will be leaked.


