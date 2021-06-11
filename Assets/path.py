import os
def set_cwd():
    cwd = os.path.dirname(os.path.abspath(__file__))
    return cwd