import os
from subprocess import call
path1 = os.getcwd()
import sys
path1 = os.path.join(path1, "Assets")
sys.path.insert(1,path1)
sys.path.insert(1,os.getcwd())
from Assets import path as p


def path():
    a = p.set_cwd()
    return a
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