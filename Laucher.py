from subprocess import call
import os
ph = os.path.join("../Aim-Trainer/Code/Game.py")
class CallPy(object):
    def __init__(self, path = ph):
        self.path = path
    def call_file(self):
        call(["Python", "{}".format(self.path)])
if __name__ == "__main__":
    c = CallPy()
    c.call_file()