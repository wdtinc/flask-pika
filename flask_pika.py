import pika
import threading
from flask import current_app

# Find the stack on which we want to store the database connection.
# Starting with Flask 0.9, the _app_ctx_stack is the correct one,
# before that we need to use the _request_ctx_stack.
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack


class Pika(object):

    def __init__(self, app=None, pika_connection_params = None):
        self.app = app
        if app is not None:
            self.init_app(app, pika_connection_params)

    def init_app(self, app, pika_connection_params):
        # Use the newstyle teardown_appcontext if it's available,
        # otherwise fall back to the request context
        if pika_connection_params is None:
            self._pika_connection_params = app.config.get('PIKA_PARAMS', None)
        else:
            self._pika_connection_params = pika_connection_params
        self._threadLocal = threading.local()
        if hasattr(app, 'teardown_appcontext'):
            app.teardown_appcontext(self.teardown)
        else:
            app.teardown_request(self.teardown)

    def create_channel(self):
        pika_connection = getattr(self._threadLocal, 'pika_connection', None)
        if pika_connection is None or not pika_connection.is_open :
            #Create connection
            pika_connection = pika.BlockingConnection(self._pika_connection_params)
            self._threadLocal.pika_connection = pika_connection
        return pika_connection.channel()

    def teardown(self, exception):
        ctx = stack.top
        if hasattr(ctx, 'pika_channel'):
            ctx.pika_channel.close()

    @property
    def channel(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'pika_channel'):
                ctx.pika_channel = self.create_channel()
            return ctx.pika_channel
