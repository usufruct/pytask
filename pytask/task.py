import json


class Task():

    def __init__(self, respond_to, secret):
        self.message = {}
        self.message['respond_to'] = respond_to
        self.message['params'] = {}
        self.message['params']['secret'] = secret

    def ping(self):
        return 'pong'

    def json_message(self):
        return json.dumps(self.message)

