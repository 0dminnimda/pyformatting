# Optional formatting

The [optional_format()](#optional_format) method, the [str.format()](https://docs.python.org/3/library/stdtypes.html#str.format) method, [OptionalFormatter](#optionalformatter) class and the [Formatter](https://docs.python.org/3/library/string.html#string.Formatter) class share the same syntax for format strings.

## optional_format

The [optional_format()](#optional_format) method is equivalent to [OptionalFormatter().format](#optionalformatter) method

Does not require entering all the variables represented by fields in the string.
The rest is [str.format](https://docs.python.org/3/library/stdtypes.html#str.format) functionality.

## OptionalFormatter

Inherits from [string.Formatter](https://docs.python.org/3/library/string.html#string.Formatter) and changes its behavior.  
Has different implementations depending on the python version. (need to change)

## Examples

Accessing arguments by position:

```python
>>> from pyformatting import optional_format
>>> optional_format('{0}{2}{1}', 'first')  # only one field will be formatted
'first{2}{1}'
>>> optional_format('first{2}{1}', '--', 'third')  # only the second argument will be used
'second{1}first'
>>> optional_format('{}{}{}', 'first')
'first{}{}'
>>> optional_format('first{}{}', '--', 'third')  # empty fields will use all arguments
'first--third'
```

Accessing arguments by name:

```python
>>> optional_format('{a}{b}{c}', a='first')
'first{b}{c}'
>>> optional_format('first{b}{c}', a='--', c='third')
'first{b}third'
```
