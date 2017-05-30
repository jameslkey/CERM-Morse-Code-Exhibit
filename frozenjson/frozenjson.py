# coding=utf-8
"""
CERMMorse : frozenjson
5/12/2017 : 3:46 PM
Author : James L. Key

-- Frozen JSON is borrowed from  “Fluent Python by Luciano Ramalho (O’Reilly).
-- Copyright 2015 Luciano Ramalho, 978-1-491-94600-8.
"""
from collections import abc
from keyword import iskeyword


class FrozenJSON:
    """
    A read-only façade for navigating a JSON-like object
    using attribute notation
    """

    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON(self.__data[name])
