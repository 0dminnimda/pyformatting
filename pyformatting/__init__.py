# -*- coding: utf-8 -*-

__version__ = "0.3.3"
__name__ = "pyformatting"


from .default_format import DefaultFormatter, defaultformatter
from .formatter import Formatter
from .optional_format import OptionalFormatter

__all__ = (
    "DefaultFormatter",
    "Formatter",
    "OptionalFormatter",
    "defaultformatter",
    "format",
    "optional_format",
)


optional_format = OptionalFormatter().format
format = Formatter().format
