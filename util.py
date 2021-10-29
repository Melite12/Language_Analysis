

import sys
import json

def sort_count_pairs(l):
    return list(sorted(l, key=cmp_to_key(cmp_count_tuples)))

def cmp_to_key(mycmp):


    class CmpFn:

        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
            return CmpFn

def cmp_count_tuples(t0, t1):

    (key0, val0) = t0
    (key1, val1) = t1
    if val0 > val1:
        return -1
    if val0 < val1:
        return 1
    if key0 < key1:
        return -1
    if key0 > key1:
        return 1
    return 0

def get_json_from_file(filename):

    try:
        return json.load(open(filename))
    except OSError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
