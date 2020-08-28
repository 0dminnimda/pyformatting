# -*- coding: utf-8 -*-

import sys
from .optional_format import OptionalFormatterNew, OptionalFormatterOld

__all__ = (
    "OptionalFormatter",
    "PY_34",
)

PY_34 = sys.version_info >= (3, 4)

if PY_34:
    OptionalFormatter = OptionalFormatterNew
else:
    OptionalFormatter = OptionalFormatterOld
