# BaseFormatter

Base class for formatters.

Has the same functionality as [string.Formatter](https://docs.python.org/3/library/string.html#string.Formatter), but is slightly faster. Also doesn't have a check_unused_args method.

To maintain backward compatibility for versions 3.4, 3.5, 3.6 BaseFormatter.format can take format_string as a keyword argument, warns DeprecationWarning.
