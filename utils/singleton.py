"""
This is a script for singleton class
"""

from typing import Any


class Singleton(type):
    """
    Metaclass that creates a Singleton base type when called.
    """
    __instances = {}
    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwds)
        return cls.__instances[cls]