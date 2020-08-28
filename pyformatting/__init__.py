# -*- coding: utf-8 -*-

__version__ = "0.2.1"
__name__ = "pyformatting"


from .optional_format import OptionalFormatter
from .default_format import DefaultFormatter, defaultformatter

__all__ = (
    "OptionalFormatter",
    "optional_format",
    "DefaultFormatter",
    "defaultformatter",
)


optional_format = OptionalFormatter().format
