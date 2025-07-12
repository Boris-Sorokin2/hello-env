# messy_code.py

import os
import sys


def my_long_function(arg1, arg2, arg3, arg4, arg5, arg6):
    print(
        "This is a very long line that will definitely exceed the 88 character limit that Black enforces by default, forcing it to be reformatted."
    )
    result = arg1 + arg2 + arg3 + arg4 + arg5 + arg6
    return result


class MyClass:
    def method_one(self):
        print("hello from method one")

    def method_two(self):
        print("hello from method two")


my_dictionary = {"key1": "value1", "key2": "value2"}

x = 10
y = 20
z = x + y
