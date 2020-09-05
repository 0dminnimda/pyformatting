# -*- coding: utf-8 -*-

from .base_formatter import BaseFormatter

__all__ = (
    "DefaultFormatter",
    "defaultformatter",
)


class DefaultFormatter(BaseFormatter):
    def __init__(self, default_factory):
        self.default_factory = default_factory

    def get_value(self, key, args, kwargs):
        if isinstance(key, int):
            if len(args) > key:
                return args[key]
        else:
            get = kwargs.get(key)
            if get is not None:
                return get

        return self.default_factory()


def defaultformatter(default_factory):
    """The default factory is called without arguments to produce
    a new value when a field value is not present.
    All remaining field are treated the same as if they were
    passed to the str.format, including keyword arguments.
    """

    return DefaultFormatter(default_factory).format
