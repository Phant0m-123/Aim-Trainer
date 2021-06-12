import os
from subprocess import call
from Assets import path

path = path.set_cwd()
ph = os.path.join(os.getcwd(), "Code/Game.py")


class CallPy(object):
    def __init__(self, path=ph, path_2="../Aim-trainer-main/Code/Game.py"):
        self.path = path
        self.path_2 = path_2

    def call_file(self):
        call(["Python", "{}".format(self.path)])

    def call_2(self):
        call(["Python", "{}".format(self.path_2)])


if __name__ == "__main__":
    c = CallPy()
    c.call_file()