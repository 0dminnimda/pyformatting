# Default formatting

further I will use "default_format" in the value of defaultformatter(some_function), where some_function is a function without input, which outputs some value, which will be used as the default.

The [default_format()](#default_format) method, the [str.format()](https://docs.python.org/3/library/stdtypes.html#str.format) method and the [DefaultFormatter](#defaultformatter) class share the same syntax for format strings.

## default_format

The [default_format()](#default_format) method is equivalent to [DefaultFormatter(some_function).format](#optionalformatter) method

The rest is [str.format](https://docs.python.org/3/library/stdtypes.html#str.format) functionality.

## DefaultFormatter

Inherits from [BaseFormatter](/base) and changes its behavior.  
