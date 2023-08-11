from contextlib import contextmanager
import ctypes
import inspect

@contextmanager
def scope():
    frame = inspect.currentframe().f_back.f_back
    loc = frame.f_locals
    before_keys = set(loc.keys())
    yield

    loc = frame.f_locals
    glob = frame.f_globals

    new_keys = [k for k in loc.keys() if k not in before_keys]
    for k in new_keys:
        del loc[k]

    ctypes.pythonapi.PyFrame_LocalsToFast(ctypes.py_object(frame), ctypes.c_int(1))


def main():
    x = 3
    with block_scope():
        y = x + 4
        print(y) # 7
        x = 8

    print(y) # UnboundLocalError

if __name__ == '__main__':
    main()
