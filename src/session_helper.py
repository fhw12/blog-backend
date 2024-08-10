from secrets import token_hex 
from time import time

class SessionHelper:
    def __init__(self):
        self.sessions = {}

    def set(self, username):
        token = token_hex(32)
        self.sessions[token] = {
            'username': username,
            'expire': time() + (60 * 60 * 24),
        }
        return token

    def get(self, token):
        if token in self.sessions:
            if self.sessions[token]['expire'] <= time():
                del self.sessions[token]
                return False
            return self.sessions[token]['username']
        return False