# -*- coding: utf-8 -*-

__all__ = ("format")


def _format(self, format_string, /, *args, **kwargs):
    return self.vformat(format_string, args, kwargs)
