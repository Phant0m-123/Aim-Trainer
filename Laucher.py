from subprocess import call
import os
class CallPy(object):
    def __init__(self, path="../Aim-Trainer/Code/Game.py"):
        self.path = path
    def call_file(self):
        call(["Python", "{}".format(self.path)])
if __name__ == "__main__":
    c = CallPy()
    c.call_file()