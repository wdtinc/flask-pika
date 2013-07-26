import pika
import threading
from flask import current_app
import warnings

# Find the stack on which we want to store the database connection.
# Starting with Flask 0.9, the _app_ctx_stack is the correct one,
# before that we need to use the _request_ctx_stack.
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack


class Pika(object):

    def __init__(self, app=None, pika_params = None):
        self.app = app
        if app is not None:
            self.init_app(app, pika_params)

    def init_app(self, app, pika_params = None):
        if pika_params is None:
            pika_params = app.config.get('PIKA_PARAMS', None)
        if 'credentials' not in pika_params:
            pika_params['credentials'] = pika.PlainCredentials(pika_params['username'], pika_params['password'])
            del pika_params['username']
            del pika_params['password']
        self._pika_connection_params = pika.ConnectionParameters(**pika_params)
        self._threadLocal = threading.local()

    def create_channel(self):
        pika_connection = getattr(self._threadLocal, 'pika_connection', None)
        if pika_connection is None or not pika_connection.is_open :
            #Create connection
            pika_connection = pika.BlockingConnection(self._pika_connection_params)
            self._threadLocal.pika_connection = pika_connection
            warnings.warn("Creating AMQP Connection")
        warnings.warn("Creating AMQP Channel")
        return pika_connection.channel()

    @property
    def channel(self):
        if self._threadLocal is not None:
            ch = getattr(self._threadLocal, 'pika_channel', None)
            if ch is None or not ch.is_open:
                ch = self.create_channel()
                self._threadLocal.pika_channel = ch
            return ch
