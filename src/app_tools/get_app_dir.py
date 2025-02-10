__version__ = '1.1.0'


import sys
import os
import inspect


def get_app_dir(return_parent_dir=False, follow_symlinks: bool=False):
    """
    Return path to __main__ (dir)
    """
    if getattr(sys, 'frozen', False): # py2exe, PyInstaller, cx_Freeze
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_app_dir)
    if follow_symlinks:
        path = os.path.realpath(path)

    app_dir = os.path.dirname(os.path.split(path)[0]) if return_parent_dir \
            else os.path.dirname((path))

    return app_dir
