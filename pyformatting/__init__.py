# -*- coding: utf-8 -*-

__version__ = "0.1.0"
__name__ = "pyformatting"


from .correct_version import OptionalFormatter

__all__ = (
    "OptionalFormatter",
    "optional_format",
)


optional_format = OptionalFormatter().format
