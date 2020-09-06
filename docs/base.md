# BaseFormatter

Base class for formatters.

Has the same functionality as [string.Formatter](https://docs.python.org/3/library/string.html#string.Formatter) as in python 3.8, but is slightly faster. Also doesn't have a check_unused_args method.

To maintain backward compatibility for python versions 3.4, 3.5, 3.6 BaseFormatter.format can take format_string as a keyword argument, warns DeprecationWarning. (not overwritten by other formaters)
