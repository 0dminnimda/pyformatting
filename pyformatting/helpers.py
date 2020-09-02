# -*- coding: utf-8 -*-

import sys

__all__ = ("PY_30", "PY_32", "PY_34", "PY_37", "PY_38")

PY_30 = sys.version_info >= (3, 0)
PY_32 = sys.version_info >= (3, 2)
PY_34 = sys.version_info >= (3, 4)
PY_37 = sys.version_info >= (3, 7)
PY_38 = sys.version_info >= (3, 8)
